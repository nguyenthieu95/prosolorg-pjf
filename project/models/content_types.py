from project import db
from datetime import datetime


class CommentMeta(db.Model):
    mete_id = db.Column(db.Integer, primary_key=True, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False, default=0, index=True)
    meta_key = db.Column(db.String(255), nullable=True, index=True)
    meta_value = db.Column(db.Text, nullable=True)

class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    comment_post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, default=0, index=True)
    comment_author = db.Column(db.Text, nullable=False, default='')
    comment_author_email = db.Column(db.String(100), nullable=False, default='', index=True)
    comment_author_url = db.Column(db.String(200), nullable=False, default='')
    comment_author_ip = db.Column(db.String(100), nullable=False, default='')
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    comment_date_gmt = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    comment_content = db.Column(db.Text, nullable=False, default='')
    comment_approved = db.Column(db.String(20), nullable=False, default='1', index=True)
    comment_agent = db.Column(db.String(255), nullable=False, default='')
    comment_type = db.Column(db.String(20), nullable=False, default='')
    comment_parent = db.Column(db.Integer, nullable=False, default=0, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=0)


class PostMeta(db.Model):
    mete_id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, default=0, index=True)
    meta_key = db.Column(db.String(255), nullable=True, index=True)
    meta_value = db.Column(db.Text, nullable=True)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_author = db.Column(db.Integer, nullable=False, default=0, index=True)
    post_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    post_date_gmt = db.Column(db.DateTime, default=datetime.utcnow)
    post_content = db.Column(db.Text, nullable=False, default='')
    post_title = db.Column(db.Text, nullable=False, default='')
    post_excerpt = db.Column(db.Text, nullable=False, default='')
    post_status = db.Column(db.String(20), nullable=False, default='publish', index=True)
    comment_status = db.Column(db.String(20), nullable=False, default='open')
    ping_status = db.Column(db.String(20), nullable=False, default='open')
    post_password = db.Column(db.String(20), nullable=False, default='')
    post_name = db.Column(db.String(200), nullable=False, default='', index=True)
    to_ping = db.Column(db.Text, nullable=False, default='')
    pinged = db.Column(db.Text, nullable=False, default='')
    post_modified = db.Column(db.DateTime, default=datetime.utcnow)
    post_modified_gmt = db.Column(db.DateTime, default=datetime.utcnow)
    post_content_filtered = db.Column(db.Text, nullable=False, default='')
    post_parent = db.Column(db.Integer, nullable=False, default=0, index=True)
    guid = db.Column(db.String(255), nullable=False, default='')
    menu_order = db.Column(db.Integer, nullable=False, default=0)
    post_type = db.Column(db.String(20), nullable=False, default='post', index=True)
    post_mime_type = db.Column(db.String(100), nullable=False, default='')
    comment_count = db.Column(db.Integer, nullable=False, default=0)
