#!/usr/bin/env python
from flask import Flask
from os import environ
import dataset

user = environ['MYSQL_USER']
pwd = environ['MYSQL_PASSWORD']
host = environ['MYSQL_HOST']
db_name = environ['MYSQL_DATABASE']

app = Flask(__name__)

db = dataset.connect('mysql://{0}:{1}@{2}/{3}'.format(user, pwd, host, db_name))
table = db['table']
table.insert(dict(first='Barry', last='Moore II'))

@app.route('/')
def hello_world():
    barry = table.find_one(first='Barry')
    return "Barry's Last Name: {}".format(barry['last'])
