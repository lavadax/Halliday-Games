import os
from flask import (
    Flask, render_template, redirect, 
    url_for, request, flash, session, abort)
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
    reviews = list(mongo.db.reviews.find().sort("review_date", -1))
    return render_template("reviews.html", reviews=reviews)

@app.route("/my_reviews/<user_id>")
def my_reviews(user_id):

    # Check if a user is logged in
    if "user" in session:

        # Check if the logged in user matches the user id from the URL variable
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})["username"]
        if session["user"] == user:
            reviews = list(mongo.db.reviews.find({"created_by": ObjectId(user_id)}))
            return render_template("reviews.html", reviews=reviews)

        flash("You're not allowed to look through this user's review list")
        abort(403, description="Page forbidden")

    flash("You're not allowed to look through this user's review list")
    abort(403, description="Page forbidden")


    

@app.route("/search", methods=["GET","POST"])
def search(): 
    if request.method == "POST":
        
        game_title = request.form.get("game_title")
        reviews = list(mongo.db.reviews.find({"game_title": game_title}).sort("score", -1))
        return render_template("search.html", reviews=reviews)

    reviews = list(mongo.db.reviews.find().sort("score", -1))
    return render_template("search.html", reviews=reviews)


@app.route("/read_review/<review_id>")
def read_review(review_id):
    if mongo.db.reviews.count_documents({"_id": ObjectId(review_id)}) == 1:

        # Check if a user is logged in
        if "user" in session:
            review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
            return render_template("read_review.html", review=review, user=session["user"])

        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        return render_template("read_review.html", review=review, user="")
    
    flash("Unable to find a review matching this ID")
    abort(404, description="Resource not Found")


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":

        # Check of a user is logged in before attempting to add a review
        if "user" in session:

            # Add review to DB
            review_details = {
                "created_by": session["user"],
                "review_date": datetime.today().strftime("%Y-%m-%d"),
                "game_title": request.form.get("game_title"),
                "review_title": request.form.get("review_title"),
                "score": request.form.get("score"),
                "review": request.form.get("review"),
                "review_summary": request.form.get("review_summary")
            }
            review = mongo.db.reviews.insert_one(review_details)
            flash("Review has been added successfully")
            return redirect(url_for("read_review", review_id=review["_id"]))


        # Redirect user as a review can't be added without logging in
        flash("Unable to add a review without logging in")
        abort(403, description="Page forbidden")
        
    # Check if a user is logged in before attempting to add a review
    if "user" in session:
        return render_template("add_review.html")

    # Redirect user as a review can't be added without logging in
    flash("Unable to add a review without logging in")
    abort(403, description="Page forbidden")


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    
    # Check if user is logged in
    if "user" in session:

        # Check if logged in user created the review
        if session["user"] == review["created_by"]:

            if request.method == "POST":
 
                new_review = {
                    "_id": ObjectId(review_id),
                    "created_by": session["user"],
                    "review_date": review["review_date"],
                    "game_title": request.form.get("game_title"),
                    "review_title": request.form.get("review_title"),
                    "score": request.form.get("score"),
                    "review": request.form.get("review"),
                    "review_summary": request.form.get("review_summary")
                }
                mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": new_review})
                flash("Review updated successfully")
                return redirect(url_for("read_review", review_id=review_id))

            return render_template("edit_review.html", review=review)
                
        # Redirect when user is trying to edit wrong review
            flash("Unable to edit another user's review")
            abort(403, description="Page forbidden") 

    # Redirect when user is not logged in
    flash("Unable to edit a review before logging in")
    abort(403, description="Page forbidden")


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


@app.route("/login", methods=["GET", "POST"])
def login():

    # Check if a user isn't logged in already
    if "user" not in session:

        if request.method == "POST":

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
        
        

        # Return for GET method
        return render_template("login.html")

    # If user is already logged in
    flash("You can't log in while logged into an account already")
    return redirect(url_for("get_account", user=session["user"]))


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
        flash("Unable to log out without logging in")
        abort(403, description="Page forbidden")
        
    


@app.route("/get_account/<user>")
def get_account(user):
    try:

        # Check if a user is logged in before attempting to get account details
        if session["user"] == user:
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            my_reviews = mongo.db.reviews.count_documents({"created_by": ObjectId(user["_id"])})
            return render_template("account.html", user=user, my_reviews=my_reviews)

        # Redirect user as account details for other accounts can't be viewed
        flash("Unable to access account details for other accounts")
        abort(403, description="Page forbidden")

    except:

        # Redirect user as account details can't be retrieved before first logging in
        flash("Unable to access account details without logging in")
        abort(403, description="Page forbidden")


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


@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 