#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    with open("/etc/config/hello") as f:
        world = f.readline().strip()
    return "Parameter: {}".format(world)
