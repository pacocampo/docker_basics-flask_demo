# -*- coding: utf-8 -*-
from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")  # decorador
def index():
    return "Hello from Flask in Docker :) with environment variable " + environ.get('MESSAGE')

@app.route("/info")
def info():
    return "Info page :) with cloud"

# Guard
if __name__ == '__main__':
    app.run(debug=environ.get('DEBUG'))
