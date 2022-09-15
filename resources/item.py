
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    #make parser part of the item so that it's easire to use in the methods
    #the parser checks to make sure the price argument is included
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "Need to include a price when entering an item")

        
    #have to authenticate before calling get method
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return item.json()
        
        #don't need else statement, logically implicit 
        return {"messaage":"Item not found"},404


    @jwt_required()
    def post(self,name):

        #check if item with that name already exists
        if ItemModel.find_by_name(name) is not None:
            return {'message':f'An item with name {name} already exists'},400
        
        #call parser after filtering name
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'])
        
        #try/except in case there was an error when inserting the data
        try: 
            item.save_to_db()
        except: 
            return {"Message":"An error occurred when inserting the item"},500
            #500 = server messed up, not user's fault 

        #always have to return json
        return item.json(), 201

    @jwt_required()
    #overwriting items list with new list that has all the items except the one that was deleted
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            item.delete_from_db(name)
            return {"Message": f"The item {item} has been deleted"}
        return {"messaage":"Item not found"},404


    @jwt_required()
    def put(self,name):
        #want to be able to update just price, so have to use parser
    
        data = Item.parser.parse_args() #instead of get_json
        #parses arguments that come through json payload and puts valid ones in data
        item = ItemModel.find_by_name(name)
      


        if item:
            #create a new one
            item = ItemModel(name, data['price'])
        else:
            item = ItemModel(name,data['price'])
            
        item.save_to_db()

        return item.json()
    

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('mycooldb.db')
        cursor = connection.cursor()

        query = '''
            SELECT * FROM items
        '''

        result = cursor.execute(query)

        items = []

        for row in result: 
            items.append({'name':row[0],'price':row[1]})

        connection.close()

        #has to be a dictionary
        return {'items':items}


#Class Methods: 
#find_by_name() --> used by get
#update() --> used by put
#insert() --> used by post