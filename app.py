import os
from flask import (
    Flask, render_template, redirect, 
    url_for, request, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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

        # Check if a user isn't logged in already
        if "user" not in session:

            # Check if username exists in db
            user = request.form.get("username")
            existing_user = mongo.db.users.find_one(
                {"username": user.lower()})
            if existing_user:
                
                # Ensure hashed password matches user input
                if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = user.lower()
                    flash("Welcome, {}".format(user))
                    return redirect(url_for(
                        "get_account", user=session["user"]))
                
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        
        # If user is already logged in
        flash("You can't log in while logged into an account already")
        return redirect(url_for("get_account", user=session["user"]))

    # Return for GET method
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Check if a user isn't logged in already
        if "user" not in session:

            # Check if the username is taken
            user = request.form.get("username").lower()
            existing_user = mongo.db.users.find_one(
                {"username": user}
            )
            if existing_user:
                flash("Username is unavailable.")
                return redirect(url_for("register"))
            
            # Check if the passwords match
            pass1 = request.form.get("password")
            pass2 = request.form.get("password2")

            if pass1 != pass2:
                flash("Passwords don't match.")
                return redirect(url_for("register"))

            # Add new user to database
            details = {
                "username": user,
                "password": generate_password_hash(pass1),
                "member_since": datetime.today().strftime("%Y-%m-%d")
            }
            mongo.db.users.insert_one(details)

            # Add the user into session cookie
            session["user"] = user.lower()
            flash("Registration successful")
            return redirect(url_for("get_account", user=session["user"]))

        # If user is already logged in
        flash("You can't create a new account while logged in")
        return redirect(url_for("get_account", user=session["user"]))

    # Return for GET method
    return render_template("register.html")


@app.route("/add_review")
def add_review():
    try:
        # Check if a user is logged in before attempting to add a review
        if session["user"]:
            return render_template("add_review.html")
    except:
        # Redirect user as a review can't be added without logging in
        # TODO replace with appropriate error handling (404 or 405)
        flash("Unable to add a review without logging in")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    try:
        # Check if a user is logged in before attempting to log out
        if session["user"]:
            flash("You've been logged out successfully")
            session.pop("user")
            return redirect(url_for("login"))
    except:
        # Redirect user as user can't be logged out before first logging in
        # TODO replace with appropriate error handling (404 or 405)
        flash("Unable to log out without logging in")
        return redirect(url_for("login"))
        
    


@app.route("/get_account/<user>")
def get_account(user):
    try:
        # TODO add top_review and top_genres variable which is a mongodb query using count & aggregate functions 
        # to pass along amount of reviews by user, and top reviewed genres by user
        # Check if a user is logged in before attempting to get account details
        if session["user"]:
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            return render_template("account.html", user=user)
    except:
        # Redirect user as account details can't be retrieved before first logging in
        # TODO replace with appropriate error handling (404 or 405)
        flash("Unable to access account details without logging in")
        return redirect(url_for("login"))


@app.route("/change_password/<user_id>", methods=["GET", "POST"])
def change_password(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    try:

        # Check if a user is logged in before attempting to get account details
        # Also checks if session username of account attempting password change
        if session["user"] == user["username"]:

            # Add form data in variables
            old_pass = request.form.get("check-password")
            new_pass = request.form.get("password")
            new_pass_check = request.form.get("password2")

            # Check if password matches current account password
            if check_password_hash(
                user["password"], old_pass):

                # Check if new password matches old password
                if old_pass == new_pass:
                    flash("New password can't be the same as old password")
                    return redirect(url_for("get_account", user=session["user"]))

                # Check if new passwords match eachother
                elif new_pass == new_pass_check:
                    new_data = {
                        "username": user["username"],
                        "password": generate_password_hash(new_pass)
                    }
                    mongo.db.users.update_one({"_id": ObjectId(user["_id"])}, {"$set": new_data})
                    flash("Password has successfully been changed")
                    return redirect(url_for("get_account", user=session["user"]))
                
                # If passwords don't match
                flash("New passwords did not match")
                return redirect(url_for("get_account", user=session["user"]))

            # If old password is incorrect
            flash("Old password is incorrect")
            return redirect(url_for("get_account", user=session["user"]))

    except:
        # Return to login page if user is not logged in
        flash("Unable to change password without logging in")
        return render_template("login")



@app.route("/read_review/<review_id>")
def read_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("read_review.html", review=review)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 