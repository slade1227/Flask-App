import re
from datetime import datetime
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")



@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
print("http://127.0.0.1:5000/hello/VSCode")# Flask-App
# Flask-App
