from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post():
    content = request.get_json(silent=True)
    return content