from flask import Flask
from flask import request

from sqlalchemy import create_engine, MetaData, Table, Column, Integer
import json

import logging
logging.basicConfig(handlers=[logging.FileHandler
                            (filename="app-server.log", 
                            encoding='utf-8', mode='a+')],
                            format="%(asctime)s %(name)s:%(levelname)s:%(message)s", 
                            datefmt="%F %A %T", 
                            level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post():
    # Parsing obtained data from Client
    content = request.get_json(silent=True)
    data = json.loads(content)
    number = data["number"]

    # Connecting to PostgreSQL DB "data"
    engine = create_engine('postgres://postgres:1@localhost:5432/data')
    meta = MetaData()

    # Table "numbers" description
    numbers = Table(
        'numbers', meta,
        Column('num', Integer),
    )

    # Checking if table "numbers" exists and creating if it's not
    meta.create_all(engine, checkfirst=True)

    # Creating Connection object
    con = engine.connect()

    # Checking if Number exists in DB
    sel = numbers.select().where(numbers.c.num == number)
    result = con.execute(sel)
    data = (-1,)
    for row in result:
        data = row

    # If Number is not in DB
    if data[0] == -1:
        # Checking if Number + 1 exists in DB
        sel = numbers.select().where(numbers.c.num == int(number) + 1)
        result = con.execute(sel)
        for row in result:
            data = row
        
        # If Number and Number + 1 are not in DB
        if data[0] == -1:
            # Adding number to "numbers" table
            try:
                ins = numbers.insert(None).values(num = number)
                result = con.execute(ins)
                content = str(int(number) + 1)
            except Exception as e:
                content = str("Error: ") + e.__str__()
        else:
            content = "Error: Number + 1 already exists in DB"
    # If Number is in DB
    else:
        content = "Error: Number already exists in DB"

    logging.info(content)    

    return content