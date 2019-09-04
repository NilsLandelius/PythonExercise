from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3


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
            item = self.find_by_name(name)
            if item:
                return item
            return {'message': 'The item does not exist'}, 404

        @classmethod    
        def find_by_name(cls,name):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "SELECT * FROM item WHERE name=?"
            result = cursor.execute(query,(name,))
            row = result.fetchone()
            connection.close()

            if row:
                return {'item': {'name':row[1],'price':row[2]}}

        @classmethod
        def insert(cls,item):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = 'INSERT INTO item (name,price) VALUES (?,?)'
            cursor.execute(query,(item['name'],item['price']))
            connection.commit()
            connection.close()
        
        @classmethod
        def update(cls,item):
                connection = sqlite3.connect('data.db')
                cursor = connection.cursor()
                query = 'UPDATE Item SET price=? WHERE name=?'
                cursor.execute(query,(item['price'],item['name']))
                connection.commit()
                connection.close()

        def post(self,name):
            parser = reqparse.RequestParser()
            parser.add_argument('price', type=float,default=0.0)
            if self.find_by_name(name):
                return{'message':"An item with name {} already exists.".format(name)}, 400

            data = parser.parse_args()    
            item = {'name': name, 'price': data['price']}

            try:
                self.insert(item)
            except:
                return {'message': 'An error occured inserting the item'}, 500
            
            return item, 201
        
        def delete(self, name):
            if not self.find_by_name(name):
                return{'message':"An item with name {} doesn't exist.".format(name)}, 400

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            del_query = 'DELETE FROM item WHERE name LIKE ?'
            cursor.execute(del_query,(name,))
            connection.commit()
            connection.close()
            return {'message':'{} was deleted'.format(name)}


        def put(self,name):
            Item.parser.add_argument('price',
                type=float,
                required=True,
                help= "This field cannot be left blank"
            )
            data = Item.parser.parse_args()
            item = {'name':name,'price':data['price']}
            if self.find_by_name(name):
                Item.update(item)
                return {'message': '{} was updated with new price'.format(name)}
            else:
                self.insert(item)
                return {'message': '{} was created'.format(name)}