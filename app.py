from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from config import config
from models import db, User
from routes.auth import auth_bp
from routes.tasks import tasks_bp

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
# Temporarily comment out CSRF for testing
# csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Add root route to redirect to login
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
