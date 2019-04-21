from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches
from . import main
from flask_login import login_required
from .forms import UpdateProfile
from .. import db,photos

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

@main.route("/<uname>")
@login_required
def new_pitch(uname):

    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("pitch.html")


@main.route("/review/<id>")
def review(id):

    return render_template("/review/review.html")


@main.route("/user/<uname>/update",methods=["GET","POST"])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form =UpdateProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for(".profile",uname=user.username))

    return render_template("profile/update.html",form=form)

'''
update photos
'''
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile= path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
