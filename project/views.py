from project import app
from flask import request, jsonify
from datetime import datetime

user = []
category = []
record = []


@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data['user_name']
    user_id = data['user_id']
    FLAG = True
    for i in range(len(user)):
        if user[i]['user_id'] == user_id:
            return 'Id is alredy exist', 400
            FLAG = False

    if FLAG:
        user.append(dict({'user_name': user_name,
                          'user_id': user_id}))
    return 'created', 200


@app.route('/create_category_record', methods=['POST'])
def create_category_record():
    data = request.get_json()
    name_category = data['name_category']
    id_category = data['id_category']
    FLAG = True
    for i in range(len(category)):
        if category[i]['name_category'] == name_category:
            FLAG = False
            return 'name_category is alredy exist', 400

        elif category[i]['id_category'] == id_category:
            FLAG = False
            return 'id_category is alredy exist', 400


    if FLAG:
        category.append(dict({'name_category': name_category,
                              'id_category': id_category}))
    return 'created', 200


@app.route('/create_expense_record', methods=['POST'])
def create_expense_record():
    data = request.get_json()
    record_id = data['record_id']
    user_id = data['user_id']
    id_category = data['id_category']
    created_date = str(datetime.now())
    sum_record = data['sum_record']
    FLAG = True
    for i in range(len(record)):
        if record[i]['record_id'] == record_id:
            FLAG = False
            return 'record_id is  alredy exist', 400
    if FLAG:
        record.append(dict({'record_id': record_id,
                            'user_id': user_id,
                            'id_category': id_category,
                            'created_date': created_date,
                            'sum_record': sum_record}))
    return 'created', 200


@app.route('/get_category', methods=['GET'])
def get_category():
    return category


@app.route('/get_list_record', methods=['GET'])
def get_list_record():
    data = request.get_json()
    user_name = data['user_name']
    list_record = []
    for i in range(len(user)):
        if user[i]['user_name'] == user_name:
            get_user_id = user[i]['user_id']

    for i in range(len(record)):
        if record[i]['user_id'] == get_user_id:
            list_record.append(record[i])

    return list_record, 200


@app.route('/get_list_category', methods=['GET'])
def get_list_category_user():
    data = request.get_json()
    user_name = data['user_name']
    name_category = data['name_category']
    list_user_category = []
    for i in range(len(user)):
        if user[i]['user_name'] == user_name:
            get_user_id = user[i]['user_id']
    for i in range(len(category)):
        if category[i]['name_category'] == name_category:
            get_category_id=category[i]['id_category']
    for i in range(len(record)):
        if record[i]['id_category'] == get_category_id and record[i]['user_id'] == get_user_id:
            list_user_category.append(record[i])
    return list_user_category


