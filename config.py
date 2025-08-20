import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class config:
    SECRET_KEY = 'your-super-secret-key-change-this-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
