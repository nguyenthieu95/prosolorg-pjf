from project import db
from datetime import datetime


class UserMeta(db.Model):
    meta = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=0)
    meta_key = db.Column(db.String(255), nullable=True, index=True)
    meta_value = db.Column(db.Text, nullable=True, index=True)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_login = db.Column(db.String(60), nullable=False, default='', index=True)
    user_pass = db.Column(db.String(64), nullable=False, default='')
    user_nicename = db.Column(db.String(50), nullable=False, default='', index=True)
    user_email = db.Column(db.String(100), nullable=False, default='')
    user_url = db.Column(db.String(100), nullable=False, default='')
    user_registered = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    user_activation_key = db.Column(db.String(60), nullable=False, default='')
    user_status = db.Column(db.Integer, nullable=False, default=0)
    display_name = db.Column(db.String(250), nullable=False, default='')




