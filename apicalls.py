import requests

def minesweeper():
    return requests.get("https://mine-sweeper-generator.herokuapp.com/solver")