import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    reviews = list(mongo.db.reviews.find())
    return render_template("search.html", reviews=reviews)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/add_review")
def add_review():
    return render_template("add_review.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 