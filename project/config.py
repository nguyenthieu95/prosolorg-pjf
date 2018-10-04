import os

class Config:
    #SECRET_KEY = os.environ.get("FLASKBLOG_SECRET_KEY")
    #SQLALCHEMY_DATABASE_URI = os.environ.get("FLASKBLOG_SQLALCHEMY_DATABASE_URI")

    SECRET_KEY = os.environ.get("FLASKBLOG_SECRET_KEY")

    POSTGRES_DEFAULT_USER = 'postgres'
    POSTGRES_USER = 'prosolorg'
    POSTGRES_PASSWORD = 'prosolorg'
    POSTGRES_DB = 'flask_prosolorg_app'
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@localhost:5432/' + POSTGRES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("FLASKBLOG_EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("FLASKBLOG_EMAIL_PASS")

