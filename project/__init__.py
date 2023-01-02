from flask_jwt_extended import JWTManager
from flask_smorest import Api
import os


from flask import Flask

from project.db import db

app = Flask(__name__)

import project.views

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
db.init_app(app)

api = Api(app)

jwt = JWTManager(app)
