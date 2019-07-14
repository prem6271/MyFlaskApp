#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Itemslist, Item
from create_table import create_table

application = Flask(__name__)
application.secret_key = 'prem'
application.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://prem:password@54.80.204.49/flaskapp'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
application.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(application)

@application.before_first_request
def create_tables():
    db.create_all()

# intialize JWT object using our app, and the 2 functions
# JWT creates a new Endpoint /auth, which gets a username and password. This gets passed to authenticate function which returns the user object when matches
# After which /auth endpoint returns a JW token
# This JW token is send during the next request, which calls the identity function
# identity function uses the JW token and gets the user_id

jwt = JWT(application, authenticate, identity)

# Item is a resource and this resource is now accessible via our api
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemslist, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(application)
    #create_table()
    application.run(port=5000, debug=True, host='0.0.0.0')
