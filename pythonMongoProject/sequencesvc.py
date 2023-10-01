from flask import Flask
import pymongo
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def root():
	return("Supported method is PUT /sequence/<name>")

@app.route("/sequence/<name>", methods=['PUT'])
def sequence(name):
    #Return a constant value
    return dumps({ name : 1})
