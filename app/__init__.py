import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "media")

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

from .models import *

with app.app_context():
    db.create_all()

from .commands import *
from .views import auth, movies

app.register_blueprint(auth, url_prefix=f"/{auth.name}")
app.register_blueprint(movies, url_prefix=f"/{movies.name}")
