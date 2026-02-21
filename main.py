from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mission Backend Started"}
@app.get("/items")
def get_items():
    return {"items": ["Laptop", "Phone", "Tablet"]}
@app.get("/about")
def about():
    return {"project": "Backend Mission", "week": 1}
from fastapi import FastAPI

app = FastAPI()
from fastapi import FastAPI
from typing import Optional  

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Mission Backend Started"}

@app.get("/about")
def about():
    return {"project": "Backend Mission", "week": 1}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

from typing import Optional

@app.get("/greet")
def greet(name: str, age: Optional[int] = None):
    return {"message": f"Hello {name}, age: {age}"}
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def root():
    return {"message": "Mission Backend Started"}
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item received successfully",
        "item": item
    }
app = FastAPI()
items_db = []
@app.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {
        "message": "Item added successfully",
        "total_items": len(items_db)
    }
@app.get("/items")
def get_items():
    return items_db
items_db = []
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
items_db = []

# Model
class Item(BaseModel):
    name: str
    price: float

# CREATE
@app.post("/items")
def create_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = len(items_db) + 1
    items_db.append(item_dict)
    return item_dict

# READ
@app.get("/items")
def get_items():
    return items_db

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for stored_item in items_db:
        if stored_item["id"] == item_id:
            stored_item["name"] = item.name
            stored_item["price"] = item.price
            return stored_item

    return {"error": "Item not found"}