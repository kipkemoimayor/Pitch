from flask import render_template
from . import main
from flask_login import login_required
@main.route("/")
def index():
    title="Pitch"
    message="Home of ideas, Where ideas are born"
    return render_template("index.html",title=title,message=message)
