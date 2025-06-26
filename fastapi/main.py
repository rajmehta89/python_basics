from typing import Union, List, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

item_list=[] 

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    item_list.append(item_dict)
    return {"message": "Item created successfully", "item": item_dict}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


