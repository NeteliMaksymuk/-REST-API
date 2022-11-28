
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from project.db import db
from project.models.category import CategoryModel
from project.schemas import CategorySchema

blp = Blueprint('category', __name__, description='Operations on category')

# GOOOD

@blp.route("/category/<int:id>/")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, id):
        category = CategoryModel.query.get_or_404(id)
        return category

@blp.route("/category")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, data):
        category = CategoryModel(**data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message='User with this name is already exist')
        return category