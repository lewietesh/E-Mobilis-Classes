from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

# this module deals with file paths
import os

# initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////home/walker/E-mobilis/march27/flaskrestful/rest.db'
app.config['SQLACLCHEMY_TRACK_MODIFICATIONS'] =False
# initialise the database
db = SQLAlchemy(app)

# initalise marshmallow 
ma = Marshmallow(app)

#  initialise class of product
class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self,name,description,price,qty):
        self.name = name
        self.description = description
        self.qty = qty

class ProductSchema(ma.Schema):
    class Meta:
        fields =('id','name','description','price','qty')

# initialise the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many =True)
@app.route('/product',methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name,description,price,qty)

    db.session.add(new_product)
    db.commit()

    return product_schema.jsonify(new_product)



@app.route('/',methods = ['GET'])
def method_name():
    return jsonify({'msg': "Hello world"})


# run the server
if __name__ == "__main__":
    app.run(debug = True)

# Flask RESTful API  summary notes
# REST stands for representational state transfer
# It’s an architectural style for designing standards between computers,
#  making it easier for systems to communicate with each other.
#  In simpler terms, REST is a set of rules developers follow when they create APIs.
#  A system is called RESTful when it adheres to these constraints.
#  To understand the term rest we need to understand the terms Client and a Resource
# Client - A client can refer to either a developer or software application which uses the API. 
#  When you are implementing the Google Maps API in your application, you are accessing resources 
# via the API, which makes you a client.Similarly, a web browser can also be a client.
# A resource describes an object, data, or piece of information that you may need to store or send to other services.

# characteristics of rest systems
# 1. Client- server  there should be a separation betweeb the server that offers the 
# serivece and the clients that consumes the service
# 2. Stateless  - the server cannot store information provided by the client in on erequest and use in another request
# 3. Cacheable - the server must indicate to the client if the request can be cached or not
# 4. Layered system - communication between the client and the server should be standardised in such a way that it allowes intermediaries to respond to
# instead of the end server, without the client having to do anythong different
# Uniform Interface - the method of communication between the client and the server must be uniform
# code on demand - servers can provide executable code or script for clients to execute in their context
# 
# 
# HTTP request methods and their actions 

# GET -	Obtain information about a resource Example:	http://example.com/api/orders
# (retrieve order list)
# GET -	Obtain information about a resource Example:	http://example.com/api/orders/123
# (retrieve order #123)
# POST -	Create a new resource Example:	http://example.com/api/orders
# (create a new order, from data provided with the request)
# PUT-	Update a resource Example:	http://example.com/api/orders/123
# (update order #123, from data provided with the request)
# DELETE-	Delete a resource	EXample: http://example.com/api/orders/123
# (delete order #123)

#  API - this stands for an application programming Interface
#  An API is a mode of communication between two software application example The google maps API 
#  An API is just a medium that lets two entities of code talk to each other.


# JSON (JavaScript Object Notation) is a text-based data storage format that is designed to be easy to read for both humans and machines.
#  JSON is generally the most common format for returning data through an API, XML being the second most common.
#  Flask provides us with a jsonify function that allows us to convert lists and dictionaries to JSON format.