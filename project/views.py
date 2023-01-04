from flask_smorest import Api

from project import app

from project.db import db
from project.resources.user import blp as UserBlueprint
from project.resources.category import blp as CategoryBlueprint
from project.resources.record import blp as RecordBlueprint


app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'Finance REST API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


api = Api(app)
with app.app_context():
    db.create_all()
api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)

