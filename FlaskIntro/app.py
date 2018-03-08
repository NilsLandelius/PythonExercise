from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


#@app.route('/',methods=["GET"]) #the slash indicates that this is the homepage of the service localhost:5000
#def home():
#    return "Hello World! " +request.args.get("username") +" and password "+request.args.get("password")

stores = [
    {
        "name":"My_wonderful_store",
        "items":[
            {
                "name":"My Item",
                "price":15.99
                }
            ]
        }
    ]


#POST /store data:{name}
@app.route("/store",methods=["POST"])
def create_store():
    request_data = request.get_json()   
    new_store = {
        "name":request_data["name"],
        "item":[]
        }
    stores.append(new_store)
    return jsonify(new_store)



#GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        return jsonify({"message":"store not found"})

@app.route("/store")
def get_stores():
    return jsonify(stores)

@app.route("/store/<string:name>/item",methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item ={
                    "item":request_data["name"],
                    "price":request_data["price"]
                    }
                
            store["items"].append(new_item)
            stores.append(store.update(new_item))
            return jsonify({"message":"new item added"})
        return jsonify({"message":"unable to add new item"})

@app.route("/store/<string:name>/item")
def get_item_in_store(name):
        for store in stores:
            if store["name"] == name:
                return jsonify({"items":store["items"]})
            return jsonify({"message":"Could not find store"})


app.run(port=5000)
