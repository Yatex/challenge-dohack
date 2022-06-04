import flask
import os
from flask import send_from_directory
from minesweeper import resolver

app = flask.Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "Not Found"

@app.route('/', methods=['GET'])
def index():
    return resolver()

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()