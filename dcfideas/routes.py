from flask import render_template
from dcfideas import app, db


@app.route("/")
def home():
    return render_template("base.html")