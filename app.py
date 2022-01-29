import os
from flask import (
    Flask, render_template, redirect, 
    url_for, request, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/search")
def search(): 
    # TODO add query & mongodb index
    reviews = list(mongo.db.reviews.find())
    return render_template("search.html", reviews=reviews)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        user = request.form.get("username")
        existing_user = mongo.db.users.find_one(
            {"username": user.lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = user.lower()
                flash("Welcome, {}".format(user))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username is taken
        user = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one(
            {"username": user}
        )

        if existing_user:
            flash("Username is unavailable.")
            return redirect(url_for("register"))
        
        # Check of the passwords match
        pass1 = request.form.get("password")
        pass2 = request.form.get("password2")

        if pass1 != pass2:
            flash("Passwords don't match.")
            return redirect(url_for("register"))

        # Add new user to database
        details = {
            "username": user,
            "password": generate_password_hash(pass1)
        }
        mongo.db.users.insert_one(details)

        # Add the user into session cookie
        session["user"] = user.lower()
        flash("Registration successful")
        return redirect(url_for("get_account", user=session["user"]))

    return render_template("register.html")


@app.route("/add_review")
def add_review():
    return render_template("add_review.html")


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/get_account/<user>")
def get_account(user):
    user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", user=user)


@app.route("/read_review")
def read_review():
    return render_template("read_review.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 