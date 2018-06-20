# coding:utf8
from . import db
import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    openid = db.Column(db.String(32), unique=True, nullable=False)
    feedbacks = db.relationship('Feedback', backref='feedbacks')

    @classmethod
    def get(cls, openid):
        return cls.query.filter_by(openid=openid).first()

    @classmethod
    def add(cls, openid):
        if openid is not None:
            user = cls()
            user.openid = openid
            db.session.add(user)
            db.session.commit()
            return user

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    id = db.Column(db.Integer, primary_key=True, index=True)
    text = db.Column(db.Unicode(140))
    post_at = db.Column(db.DateTime)

    @classmethod
    def add(cls, text):
        feedback = cls()
        feedback.post_at = datetime.datetime.now()
        feedback.text = text
        db.session.add(feedback)
        db.session.commit()
        return  feedback