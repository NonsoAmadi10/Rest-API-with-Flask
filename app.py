from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize a Flask Server
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

## Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db 
db = SQLAlchemy(app)

# Initialize Marshmallow
marsh = Marshmallow(app)


# Inventory Class/Model

class Inventory(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(80), unique=True, nullable=False)
  created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  qty= db.Column(db.Integer)


  def __init__(self, name, created_on, qty):
   self.name = name
   self.created_on = created_on
   self.qty = qty 



# Inventory Schema 

class InventorySchema(marsh.Schema):
  class Meta:
   fields = ('id', 'name', 'created_on', 'qty')

# Initialize Schema

inventory_schema = InventorySchema(strict=True)
inventories_schema = InventorySchema(many=True, strict=True)



## Home Route 

@app.route('/', methods=['GET'])
def get():
  return jsonify({ "message": "Welcome to Flask"})


@app.route('/inventory', methods=['POST'])
def add_inventory():
 name= request.json['name']
 qty= request.json['qty']
 created_on = datetime.now()

 new_inventory = Inventory(name, created_on, qty)

 db.session.add(new_inventory)
 db.session.commit()

 return inventory_schema.jsonify(new_inventory)


@app.route('/inventory', methods=['GET'])
def get_all_inventory():
 all_inventory = Inventory.query.all()

 return inventories_schema.jsonify(all_inventory)







 # Run the Server
if __name__ == '__main__':
  app.run(debug=True)