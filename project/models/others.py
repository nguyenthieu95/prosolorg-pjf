from project import db
from datetime import datetime

class Links(db.Model):
    link_id = db.Column(db.Integer, primary_key=True, nullable=False)
    link_url = db.Column(db.String(255), nullable=False, default='')
    link_name = db.Column(db.String(255), nullable=False, default='')
    link_image = db.Column(db.String(255), nullable=False, default='')
    link_target = db.Column(db.String(25), nullable=False, default='')
    link_description = db.Column(db.String(255), nullable=False, default='')
    link_visible = db.Column(db.String(20), nullable=False, default='Y', index=True)
    link_owner = db.Column(db.Integer, nullable=False, default=1)
    link_rating = db.Column(db.Integer, nullable=False, default=0)
    link_updated = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    link_rel = db.Column(db.String(255), nullable=False, default='')
    link_notes = db.Column(db.Text, nullable=False, default='')
    link_rss = db.Column(db.String(255), nullable=False, default='')

class Options(db.Model):
    option_id = db.Column(db.Integer, primary_key=True, nullable=False)
    option_name = db.Column(db.String(64), nullable=False, default='', unique=True)
    option_value = db.Column(db.Text, nullable=False, default='')
    autoload = db.Column(db.String(20), nullable=False, default='yes')
