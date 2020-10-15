from fastapi import FastAPI
from fastapi import HTTPException
from mongo import Database
from typing import Optional

database = Database()
app = FastAPI(title="RentBase")

@app.get("/get")
def read_root():
    try:
        result = database.printing()
    except (TypeError, ValueError):
        raise HTTPException(404, 'Failed to load db')
    return result 



