from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.item import ItemModel

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
            i.save_to_db()
        except:
            return {"message": "An error occurred."}, 500 # code for internal error

        return i.json(), 201

    #@jwt_required()
    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}
    #@jwt_required()
    def put(self, name):
        req = Item.parser.parse_args()

        i = ItemModel.get_item_by_name(name)
        if i is None:
            i = ItemModel(name, req['price'])
        else:
            i.price = req['price']

        i.save_to_db()

        return i.json(), 201

class Itemslist(Resource):
    #@jwt_required()
    def get(self):
        return {'items': [i.json() for i in ItemModel.query.all()]}, 200
