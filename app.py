import os
from flask import Flask
from jinja2.utils import markupsafe

app = Flask(__name__)

@app.route('/')
def response():
    return "hello world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 
