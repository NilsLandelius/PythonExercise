from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'nils'
api = Api(app)

jwt = JWT(app,authenticate,identity)

items = []

class ItemList(Resource):
    def get(self):
        return {'items':items} 

class Item(Resource):
        @jwt_required()
        def get(self,name):
            item = next(filter(lambda x :x['name']==name, items),None)
            return {'item':item}, 200 if item else 404

        def post(self,name):
            parser = reqparse.RequestParser()
            parser.add_argument('price', type=float,default=0.0)
            if next(filter(lambda x :x['name']==name, items),None):
                return{'message':"An item with name {} already exists.".format(name)}, 400

            data = parser.parse_args()    
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201
        
        def delete(self, name):
            global items
            checkList = []
            for item in items:
                checkList.append(item['name'])
            if name not in checkList:
                return {'message': 'Item not found'}
            else:
                del items[checkList.index(name)]
                return {'message': '{} deleted'.format(name)}

        def put(self,name):
            parser = reqparse.RequestParser()
            parser.add_argument('price',
                type=float,
                required=True,
                help= "This field cannot be left blank"
            )
            data = parser.parse_args()

            item = next(filter(lambda x: x['name']==name,items),None)
            if item is None:
                item = {'name': name, 'price':data['price']}
                items.append(item)
            else:
                item.update(data)
            return item

api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')

app.run(port=5000, debug=True)