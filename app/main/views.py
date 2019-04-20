from flask import render_template
from . import main
@main.route("/")
def index():
    title="Pitch"
    message="Home of ideas"
    return render_template("index.html",title=title,message=message)
