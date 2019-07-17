from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize a Flask Server
app = Flask(__name__)


## Home Rout

@app.route('/', methods=['GET'])
def get():
  return jsonify({ "message": "Welcome to Flask"})
 # Run the Server
if __name__ == '__main__':
  app.run(debug=True)