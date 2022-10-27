import profile
from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User
from flask_login import LoginManager

from .auth.routes import auth
from .profiles.routes import profile
from .monsters.routes import monsters
from .create_roster.routes import createRoster


app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(monsters)
app.register_blueprint(createRoster)

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

login.login_view = 'auth.logIn'

from . import routes
from . import models