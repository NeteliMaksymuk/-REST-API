from project import app
from flask import request, jsonify
# /create_user
# /create_category_record
# /create_expense_record
# /get_category
# /get_list_record/<user>/
# /get_list_category/<user>/
user = []
category = []
record = []


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    id = data['id']
    FLAG = True
    for i in range(len(user)):
        if user[i]['id'] == id:
            return 'Id is alredy exist', 400
            FLAG = False

    if FLAG:
        user.append(dict({'name': name, 'id': id}))
    return 'created', 200


@app.route('/create_category_record', methods=['POST'])
def create_category_record():
    pass


@app.route('/create_expense_record', methods=['POST'])
def create_expense_record():
    pass


@app.route('/get_category', methods=['GET'])
def get_category():
    pass


@app.route('/get_list_record', methods=['GET'])
def get_list_record():
    pass


@app.route('/get_list_category', methods=['GET'])
def creatget_list_categorye_user():
    pass


