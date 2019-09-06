from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3
from models.item import ItemModel


class ItemList(Resource):
    def get(self):
        itemlist = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT name, price FROM item"
        for row in cursor.execute(query):
            itemlist.append({'name':row[0],'price':row[1]})
        
        connection.commit()
        connection.close()
         
        
        return {'items':itemlist} 

class Item(Resource):
        parser = reqparse.RequestParser()
        @jwt_required()
        def get(self,name):
            item = ItemModel.find_by_name(name)
            if item:
                return item.json()
            return {'message': 'The item does not exist'}, 404

        def post(self,name):
            parser = reqparse.RequestParser()
            parser.add_argument('price', type=float,default=0.0)
            if ItemModel.find_by_name(name):
                return{'message':"An item with name {} already exists.".format(name)}, 400

            data = parser.parse_args()    
            item = ItemModel(name,data['price'])

            try:
                item.save_to_db()
            except:
                return {'message': 'An error occured inserting the item'}, 500
            
            return item.json(), 201
        
        def delete(self, name):
            item = ItemModel.find_by_name(name)
            if item:
                item.delete_from_db()
            
            return {'message':'Item deleted'}
                


        def put(self,name):
            Item.parser.add_argument('price',
                type=float,
                required=True,
                help= "This field cannot be left blank"
            )
            data = Item.parser.parse_args()
            item = ItemModel(name,data['price'])
            if ItemModel.find_by_name(name):
                item.save_to_db()
                return {'message': '{} was created'.format(name)}