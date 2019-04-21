from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches,Comments
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile,WritePitch,ReviewForm
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
    pitch=Pitches.query.filter_by(author=uname).all()
    return render_template("profile/profile.html",user=user,pitch=pitch)

'''
new Pitch idea
'''

@main.route("/<uname>",methods=["GET","POST"])
@login_required
def new_pitch(uname):
    uname=uname
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form=WritePitch()
    if form.validate_on_submit():
        new_pitch=Pitches(pitch=form.pitch.data,title=form.title.data,author=uname)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for(".index"))
        title="new Pitch"

    return render_template("pitch.html",new_review=form)

'''
review
'''

@main.route("/pitch/new/review/<int:id>",methods=["GET","POST"])
@login_required
def review(id):
    pitch_id=id
    pitch=Pitches.query.all();
    title="Write a comment"
    form=ReviewForm()
    if form.validate_on_submit():
        title=form.title.data
        comments=form.comments.data

        #update this variables
        review=Comments(pitch_id=id,pitch_title=title,comments=comments,user=current_user)

        #save
        review.save_comment()
        return redirect(url_for('.review',id=pitch_id))


    return render_template("new_review.html",pitch=pitch,id=pitch_id,title=title,comment_form=form)


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
