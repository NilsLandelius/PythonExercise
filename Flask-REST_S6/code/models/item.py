import sqlite3
from db import db

class ItemModel(db.Model):
    def __init__(self,name,price):
        self.name = name
        self.price = price
    

    def json(self):
        return {'name': self.name,'price': self.price}
    
    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM item WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(row[1],row[2])
            

    
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO item (name,price) VALUES (?,?)'
        cursor.execute(query,(self.name,self.price))
        connection.commit()
        connection.close()
    
    
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE Item SET price=? WHERE name=?'
        cursor.execute(query,(self.price,self.name))
        connection.commit()
        connection.close()