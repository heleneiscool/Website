import sys
from flask import Flask, render_template
print(sys.path)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/enroll")
def enroll():
    return render_template("enroll.html")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
