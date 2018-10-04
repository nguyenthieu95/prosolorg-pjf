from project import db

class Terms(db.Model):
    term_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(200), nullable=False, default='', index=True)
    slug = db.Column(db.String(200), nullable=False, default='', unique=True)
    term_group = db.Column(db.Integer, nullable=False, default=0)


class TermMeta(db.Model):
    meta_id = db.Column(db.Integer, primary_key=True, nullable=False)
    term_id = db.Column(db.Integer, nullable=False, default=0, index=True)
    meta_key = db.Column(db.String(255), nullable=True, index=True)
    meta_value = db.Column(db.Text, nullable=True)


class TermRelationships(db.Model):
    object_id = db.Column(db.Integer, primary_key=True, nullable=False, default=0)
    term_taxonomy_id = db.Column(db.Integer, primary_key=True, nullable=False, index=True, default=0)
    term_order = db.Column(db.Integer, nullable=False, default=0)


class TermTaxonomy(db.Model):
    term_taxonomy_id = db.Column(db.Integer, primary_key=True, nullable=False)
    term_id = db.Column(db.Integer, primary_key=True, nullable=False, default=0, unique=True)
    taxonomy = db.Column(db.String(32), nullable=False, default='', unique=True, index=True)
    description = db.Column(db.Text, nullable=False, default='')
    parent = db.Column(db.Integer, nullable=False, default=0)
    count = db.Column(db.Integer, nullable=False, default=0)


