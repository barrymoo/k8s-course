#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

version = "v2"

@app.route('/')
def root():
    return version

@app.route('/v1')
def v1():
    return version

@app.route('/v2')
def v2():
    return version
