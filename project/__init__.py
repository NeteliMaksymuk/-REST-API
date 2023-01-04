from flask_jwt_extended import JWTManager
from flask_smorest import Api
import os


from flask import Flask, jsonify

from project.db import db

app = Flask(__name__)

import project.views
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_SECRET_KEY"] = str(os.getenv("JWT_SECRET_KEY"))
print(os.getenv("JWT_SECRET_KEY"))

db.init_app(app)

api = Api(app)

jwt = JWTManager(app)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return (
       jsonify({"message": "The token has expired.", "error": "token_expired"}),
       401,
   )

@jwt.invalid_token_loader
def invalid_token_callback(error):
   return (
       jsonify(
           {"message": "Signature verification failed.", "error": "invalid_token"}
       ),
       401,
   )

@jwt.unauthorized_loader
def missing_token_callback(error):
   return (
       jsonify(
           {
               "description": "Request does not contain an access token.",
               "error": "authorization_required",
           }
       ),
       401,
   )
