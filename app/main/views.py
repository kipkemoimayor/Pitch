from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches
from . import main
from flask_login import login_required
@main.route("/")
def index():
    title="Pitch"
    message="Home of ideas, Where ideas are born"
    pitch=Pitches.query.all();

    return render_template("index.html",title=title,message=message,pitch=pitch)
