from fastapi import FastAPI
from fastapi import HTTPException
from mongo import Database

app = FastAPI(title="RentBase")

@app.get("/get")
def get_anything():
    return Database.printing()
