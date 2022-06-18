from flask import render_template
from dcfideas import app, db
from dcfideas.models import Strand, Element, Camcynnydd, Aole, Idea 


@app.route("/")
def home():
    return render_template("base.html")