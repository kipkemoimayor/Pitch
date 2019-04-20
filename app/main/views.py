from flask import render_template
from . import main
@main.route("/")
def index():
    title="Pitch"
    message="Home of ideas, Where ideas are born"
    return render_template("index.html",title=title,message=message)
