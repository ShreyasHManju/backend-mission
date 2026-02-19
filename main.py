from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mission Backend Started"}
@app.get("/items")
def get_items():
    return {"items": ["Laptop", "Phone", "Tablet"]}

