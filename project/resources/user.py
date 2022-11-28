from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from project.db import db
from project.models.user import UserModel
from project.schemas import UserSchema

blp = Blueprint('user', __name__, description='Operations on user')

#GOOD
@blp.route("/user/<int:id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user


#GOOD
@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, data):
        user = UserModel(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message='User with this name is already exist')
        return user

