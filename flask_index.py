from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello,digigan'


app.run(host='localhost', port='8080')
