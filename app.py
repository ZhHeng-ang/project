import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "666"

# app.run(host="127.0.0.1",port="8000")