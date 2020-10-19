import ast
from fastapi import FastAPI
from fastapi import HTTPException
from mongo import Database
from typing import Optional
from bson.objectid import ObjectId
from properties import OPTIONS, NAME
from fastapi.middleware.cors import CORSMiddleware


database = Database()
app = FastAPI(title=NAME)

origins = [
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/objects")
async def read_root():
    try:
        a = database.cherta(database.objects_collection, {}, OPTIONS)
    except (TypeError, ValueError):
        raise HTTPException(404, 'Failed to load db')
    return a

@app.get("/search/")
async def read_user_item( adress: str):
    try:
        a = database.search_objects(database.objects_collection, adress, OPTIONS)
    except(TypeError, ValueError):
        raise HTTPException(404, 'Failed to load DB')
    return a

