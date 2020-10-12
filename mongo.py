import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient('192.168.2.195', 27017)
db = client.RentBase
objects_collection = db.object
def find_document(collection, elements, multiple=True):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)
def insert_document(collection, data):
    return collection.insert_one(data).inserted_id
def delete_document(collection, query):
    collection.delete_one(query)
def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})
def printing():
    results = find_document(objects_collection, {})
    for result in results:
        print(result)
def cherta():
    print(f"{'='*50}")


