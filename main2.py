# 1 行目
# from fastapi import FastAPI, Query
# from typing import Annotated

# app = FastAPI()

# items = ["Tシャツ", "スカート", "ブーツ", "コート"]

# @app.get("/items")
# def read_items(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
#     return{"items": items[skip : skip + limit]}

# @app.get("/items/{item_id}")
# def read_items(
#     item_id: str,
#     skip: int,
#     limit: Annotated[int, Query(ge=1, le=10)] = 10
# ):
#     return{"items": items[skip : skip + limit]}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Item(BaseModel):
    name: str,
    price: float,
    description: Union[str, None] = None
    

@app.post("/items")
def create_item(Item* Item):
    print(f"")
    
