import pymongo
import typing
import random
import ast
import pydantic
from bson.objectid import ObjectId
from properties import DBADDRESS

class Database:

    def __init__(self):
        self.client = pymongo.MongoClient(DBADDRESS, 27017)
        self.db = self.client.Counters
        self.objects_collection = self.db.object
    
    def find_document(self,collection, elements, multiple=True):
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            return collection.find_one(elements)


    def insert_document(self,collection, data):
        return collection.insert_one(data).inserted_id


    def delete_document(self, collection, query):
        collection.delete_one(query)


    def update_document(self,collection, query_elements, new_values):
        collection.update_one(query_elements, {'$set': new_values})


    def printing(self):
        results = self.find_document(self.objects_collection, {})
        return results


    def cherta(self,collection,elements,options,multiple=True):
        a = collection.find(elements, options)
        return list(a)

    def parse_address(self, collection):
        a = collection.find({})
        b=''
        for entr in a:
            b = entr['address'].split()
            for el in b:
                if el == 'г.Новосибирск':
                    b.remove('г.Новосибирск')
            new_address = ' '.join(b)
            new_values = {'address' : new_address}
            print(entr)
            self.update_document(collection, entr, new_values)

    def search_objects(self, collection, adress, options={}):
        a = collection.find({})
        b = ''
        result = []
        for entr in a:
            b = entr['address'].split()
            for el in b:
                if el == adress:
                    serch_res = collection.find(entr,options)
                    result += serch_res
        return result

d = Database()
'''
d.parse_address(d.objects_collection)
print(d.search_objects(d.objects_collection, 'Учительская'))
'''
