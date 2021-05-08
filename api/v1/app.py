#!/usr/bin/python3
"""Status of your API"""

from flask import Flask, Blueprint
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def task0(exception):
    """get the status of this page """
    storage.close()


@app.errorhandler(404)
def get_404(e):
    """get the status of this page """
    mydict = {"error": "Not found"}
    return mydict

if __name__ == "__main__":
    hosta = getenv("HBNB_API_HOST")
    porta = getenv("HBNB_API_PORT")

    if hosta is None:
        hosta = "0.0.0.0"
    if porta is None:
        porta = 5000
    app.run(host=hosta, port=porta, debug=True, threaded=True)
