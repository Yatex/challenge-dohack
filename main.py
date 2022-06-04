from flask import Flask
from minesweeper import resolver


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "Not Found"

@app.route('/', methods=['GET'])
def index():
    return resolver()