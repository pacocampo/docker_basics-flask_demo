# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")  # decorador
def index():
    return "Hello from Flask in Docker :)"

@app.route("/info")
def info():
    return "Info page :)"

# Guard
if __name__ == '__main__':
    app.run(debug=True)
