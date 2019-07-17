# Rest-API-with-Flask
A simple rest api created with the flask framework


### Tools 
- Flask - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
- SQLALCHEMY - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

- FLASK-MARSHMALLOW - Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) integrates with Flask-SQLAlchemy.


- SQLITE -SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. 


## Getting Started
- Clone this repo 
  `` Run pip3 install pipenv `` 
  then 
  `` Run pipenv install `` to install all dependencies

  - Start the server by running ` python app.py `

### Testing the endpoints
- Open postman on ` localhost:5000/ `
- The following endpoints and request body are found in the table below

| Endpoints | Request |Description|
|-----------|---------|-----------|
| POST /inventory/| ``{ "name": "Milk","qty": "2000"}``| adds an inventory|
|GET/inventory/id| none| Gets a specific inventory record|
|GET /inventory| none | Gets all inventory records |
| PATCH /inventory/qty/id| ` {"qty": "7000"}`| Updates the quantity of an inventory |
| DELETE /inventory/id | none | Deletes an inventory record |


### Author 
- Chinonso Amadi
 