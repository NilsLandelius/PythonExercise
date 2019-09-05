import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',required=True, type=str, help="This field cannot be blank")
    parser.add_argument('password',type=str,default='password')

    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message':'User already exists'}, 400
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "User was created successfully"}, 201