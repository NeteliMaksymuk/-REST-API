from project import app

# /create_user
# /create_category_record
# /create_expense_record
# /get_category
# /get_list_record/<user>/
# /get_list_category/<user>/
user = {}
category = {}
record = {}


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/create_user', methods=['POST'])
def create_user():
    pass


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


