from flask import *


@app.route('/')
def hello_world():
    return 'Hello, World!'


app = Flask(__name__)
