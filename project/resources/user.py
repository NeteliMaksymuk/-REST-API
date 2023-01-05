from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint, abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

from project.db import db
from project.models.user import UserModel
from project.schemas import UserSchema

blp = Blueprint('user', __name__, description='Operations on user')


@blp.route("/user/<int:id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user


@blp.route("/register")
class UserList(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, data):
        user = UserModel(
            name=data["name"], password=pbkdf2_sha256.hash(data["password"]),
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message='User with this name is already exist')
        return user


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, data):
        user = UserModel(
            name=data["name"], password=pbkdf2_sha256.hash(data["password"]),
        )
        if user and pbkdf2_sha256.verify(data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        abort(402, message='Uncorrected name of password')