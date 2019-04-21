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


@main.route("/user/<uname>")
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html",user=user)

'''
new Pitch idea
'''

@main.route("/pitch/<uname>")
@login_required
def new_pitch(uname):

    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("new_pitch/pitch.html")


@main.route("/review/<id>")
def review(id):

    return render_template("/review/review.html")
