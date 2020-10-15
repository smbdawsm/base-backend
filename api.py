from fastapi import FastAPI
from fastapi import HTTPException
from mongo import Database
from typing import Optional
import ast
from bson.objectid import ObjectId
from properties import OPTIONS, NAME

database = Database()
app = FastAPI(title=NAME)

@app.get("/objects")
def read_root():
    try:
        a = database.cherta(database.objects_collection, {}, OPTIONS)
    except (TypeError, ValueError):
        raise HTTPException(404, 'Failed to load db')
    return a


