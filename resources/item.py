from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.item import ItemModel
import mysql.connector

items = []

# Our 1st Resource with only get method.
class Item(Resource):
    # Instead of creating the parser for each method, we should have it in the class level
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be empty!"
    )
    #@jwt_required()   # this can be added for any http request method
    def get(self, name):
        item = ItemModel.get_item_by_name(name)
        if item:
            return item.json(), 200
        return {'Message' : 'Item not found'}, 404

    #@jwt_required()
    def post(self, name):
        if ItemModel.get_item_by_name(name):
            return {'Message' : "Item '{}' already exists".format(name)}, 400

        req = Item.parser.parse_args()
        i = ItemModel(name, req['price'])
        try:
            i.insert()
        except:
            return {"message": "An error occurred."}, 500 # code for internal error

        return i.json(), 201

    #@jwt_required()
    def delete(self, name):
        connect_var = mysql.connector.connect(host='100.24.14.5',
         database='flaskapp',
         user='prem',
         password='password', ssl_disabled='False')
        cursor = connect_var.cursor()
        del_query = "DELETE from items where name = %s"

        cursor.execute(del_query, (name,))

        connect_var.commit()
        cursor.close()
        connect_var.close()
        return {"message": "Item deleted."}

    #@jwt_required()
    def put(self, name):
        req = Item.parser.parse_args()
        i = ItemModel(name, req['price'])

        if ItemModel.get_item_by_name(name):
            try:
                i.update()
            except:
                return {"message": "An error occurred."}, 500 # code for internal error
        else:
            try:
                i.insert()
            except:
                return {"message": "An error occurred."}, 500 # code for internal error

        return i.json(), 201

class Itemslist(Resource):
    @jwt_required()
    def get(self):
        conn = mysql.connector.connect(host = '100.24.14.5',
            database = 'flaskapp',
            user = 'prem',
            password = 'password', ssl_disabled='False')
        cursor = conn.cursor()
        query = "SELECT * FROM items"
        cursor.execute(query)
        result = cursor.fetchall()
        items = []
        for i in result:
            items.append(i)
        cursor.close()
        conn.close()
        if result:
            return {"items": items}, 200
