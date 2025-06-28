from typing import Union, List, Dict, Any
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

app = FastAPI()

# Define the SQLAlchemy database engine and session
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the SQLAlchemy declarative base
Base = declarative_base()

# Define the Item model
class Item(Base):
    __tablename__ = "items"

    def __init__(self, name: str, description: Union[str, None] = None, price: float = 0.0, tax: Union[float, None] = None):
        self.name = name
        self.description = description
        self.price = price
        self.tax = tax

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.delete("/items/{name}")
def delete_item(name:str):
    db = SessionLocal()
    item = db.query(Item).filter(Item.name == name).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{name}")
def update_item(name:str, item:Item):
    db = SessionLocal()
    existing_item = db.query(Item).filter(Item.name == name).first()
    if existing_item:
        existing_item.name = item.name
        existing_item.description = item.description
        existing_item.price = item.price
        existing_item.tax = item.tax
        db.commit()
        return existing_item
    raise HTTPException(status_code=404, detail="Item not found")
    

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/")
def create_item(item: Item):
    db = SessionLocal()
    db_item = Item(name=item.name, description=item.description, price=item.price, tax=item.tax)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item created successfully", "item": db_item}

@app.get("/items/{name}")
def get_item_by_name(name:str):

    db = SessionLocal()
    item = db.query(Item).filter(Item.name == name).first()
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/health")
def health_check():
    return {"status": "healthy"}


