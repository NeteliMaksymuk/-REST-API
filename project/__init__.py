# flask  --app __init__ run
from flask import Flask

app = Flask(__name__)

import project.views
