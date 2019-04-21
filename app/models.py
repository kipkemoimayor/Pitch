from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(250),index=True)
    email=db.Column(db.String(250),unique=True,index=True)
    pass_secure=db.Column(db.String(255))
    about=db.Column(db.String(500))
    profile=db.Column(db.String(250))

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")
    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'

'''
Pitch ideas table
'''

class Pitches(db.Model):
    __tablename__="pitches"
    id=db.Column(db.Integer,primary_key=True)
    pitch=db.Column(db.String(500))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return f'User {self.pitch}'


class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(250))
    pitches=db.relationship('Pitches',backref='category',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
