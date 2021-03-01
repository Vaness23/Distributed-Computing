from flask import Flask
from flask import request

from sqlalchemy import create_engine
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post():
    content = request.get_json(silent=True)
    data = json.loads(content)
    if data["number"] == "23":
        engine = create_engine('postgres://postgres:1@localhost:5432/data')

        with engine.connect() as con:
            res = con.execute('SELECT * FROM "posts";')

            for row in res:
                print(row)
                data["number"] = row[1]
    else:
        data["number"] = "No DB info"

    content = json.dumps(data)
    return str(data)