import pymongo
import typing
import random
import ast
import pydantic
from bson.objectid import ObjectId
from properties import DBADDRESS

class Database:
    client = pymongo.MongoClient(DBADDRESS, 27017)
    db = client.RentBase
    objects_collection = db.object
    
    def find_document(self,collection, elements, multiple=True):
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            return collection.find_one(elements)


    def insert_document(self,collection, data):
        return collection.insert_one(data).inserted_id


    def delete_document(self,collection, query):
        collection.delete_one(query)


    def update_document(self,collection, query_elements, new_values):
        collection.update_one(query_elements, {'$set': new_values})


    def printing(self):
        results = self.find_document(self.objects_collection, {})
        return results


    def cherta(self,collection,elements,options,multiple=True):
        a = collection.find(elements, options)
        return list(a)