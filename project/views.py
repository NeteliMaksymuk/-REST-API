from flask_smorest import Api

from project import app
from flask import request, jsonify, abort
from datetime import datetime

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
# app.config[''] = ''

api = Api(app)
with app.app_context():
    db.create_all()
api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)


# # все що знизу можна дел якщо перенесла все в ресурси
#
# user = []
# category = []
# record = []
#
#
# @app.route('/create_user', methods=['POST'])
# def create_user():
#     data = request.get_json()
#
#     if ('user_id' not in data
#             and 'user_name' not in data):
#         abort(400, message="Bad request, some data is required.")
#
#     user_name = data['user_name']
#     user_id = data['user_id']
#     for i in range(len(user)):
#         if user[i]['user_id'] == user_id:
#             abort(400, message='Id is already exist')
#
#     user.append(dict({'user_name': user_name,
#                       'user_id': user_id}))
#     return 'created', 200
#
#
# @app.route('/create_category_record', methods=['POST'])
# def create_category_record():
#     data = request.get_json()
#
#     if ('name_category' not in data
#             or 'id_category' not in data):
#         abort(400, message="Bad request, some data is required.")
#
#     name_category = data['name_category']
#     id_category = data['id_category']
#
#     for i in range(len(category)):
#         if category[i]['name_category'] == name_category:
#             abort(400, message='name_category is already exist')
#
#         elif category[i]['id_category'] == id_category:
#             abort(400, message='id_category is already exist')
#
#     category.append(dict({'name_category': name_category,
#                           'id_category': id_category}))
#     return 'created', 200
#
#
# @app.route('/create_expense_record', methods=['POST'])
# def create_expense_record():
#     data = request.get_json()
#     if ('record_id' not in data
#             or 'id_category' not in data
#             or 'user_id' not in data):
#         abort(400, message="Bad request, some data is required.")
#     if data['user_id'] not in user:
#         abort(400, message="This user is not exist.")
#     record_id = data['record_id']
#     user_id = data['user_id']
#     id_category = data['id_category']
#     created_date = str(datetime.now())
#     sum_record = data['sum_record']
#
#     for i in range(len(record)):
#         if record[i]['record_id'] == record_id:
#
#             return 'record_id is  alredy exist', 400
#
#     record.append(dict({'record_id': record_id,
#                         'user_id': user_id,
#                         'id_category': id_category,
#                         'created_date': created_date,
#                         'sum_record': sum_record}))
#     return 'created', 200
#
#
# @app.route('/get_category', methods=['GET'])
# def get_category():
#     return category
#
#
# @app.route('/get_list_record', methods=['GET'])
# def get_list_record():
#     data = request.get_json()
#     user_name = data['user_name']
#     list_record = []
#     for i in range(len(user)):
#         if user[i]['user_name'] == user_name:
#             get_user_id = user[i]['user_id']
#
#     for i in range(len(record)):
#         if record[i]['user_id'] == get_user_id:
#             list_record.append(record[i])
#
#     return list_record, 200
#
#
# @app.route('/get_list_category', methods=['GET'])
# def get_list_category_user():
#     data = request.get_json()
#     user_name = data['user_name']
#     name_category = data['name_category']
#     list_user_category = []
#     for i in range(len(user)):
#         if user[i]['user_name'] == user_name:
#             get_user_id = user[i]['user_id']
#     for i in range(len(category)):
#         if category[i]['name_category'] == name_category:
#             get_category_id = category[i]['id_category']
#     for i in range(len(record)):
#         if record[i]['id_category'] == get_category_id and record[i]['user_id'] == get_user_id:
#             list_user_category.append(record[i])
#     return list_user_category
