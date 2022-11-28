from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from project.db import db
from project.models import RecordModel, CategoryModel
from project.schemas import RecordSchema, RecordQuerySchema

blp = Blueprint('record', __name__, description='Operations on record')


@blp.route("/record/<int:id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, id):
        record = RecordModel.query.get_or_404(id)
        return record


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location='query', as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get('user_id')
        if not user_id:
            abort(400, message='User with this name is not exist')
        query = RecordModel.query.filter(user_id == user_id)
        category_id = kwargs.get('category_id')
        if not category_id:
            query = RecordModel.query.filter(category_id == category_id)
        return query.all()

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, data):
        record = RecordModel(**data)
        category = CategoryModel.query.get_or_404(data['category_id'])
        created_by = getattr(category, "created_by")
        try:
            if data['user_id'] == created_by or created_by is None:
                db.session.add(record)
                db.session.commit()
            else:
                abort(400, message='You are not owner of this category')

        except IntegrityError:
            abort(400, message='Record error')
        return record