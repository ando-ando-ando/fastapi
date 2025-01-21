import uvicorn
from typing import List, Union, Annotated
from enum import Enum
from fastapi import FastAPI, Path ,Query
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def root():
    return {"message": "post"}

@app.put("/")
async def root():
    return {"message": "put"}

@app.delete("/")
async def root():
    return {"message": "delete"}

# パスパラメータ
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id" : item_id}

# パスパラメータと型
# int型
@app.get("/items_int/{item_id_int}")
async def read_item(item_id_int: int):
    return {"item_id_int" : item_id_int}

# 順序の問題
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
    
    
# リクエストボディ

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# クエリパラメータと文字列の検証
# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(
#         default=None, min_length=3, max_length=50, pattern="^fixedquery$"
#         )
#     ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default=None)):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# デバック用途
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

items = ["Tシャツ", "スカート", "ブーツ", "コート"]

# @app.get("/items")
# def read_items(
#     item_id: str,
#     skip: 
# )

def read_items(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
    return{"items": items[skip : skip + limit]}
