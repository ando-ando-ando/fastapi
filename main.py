import uvicorn
from typing import Union
from enum import Enum
from fastapi import FastAPI
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
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}

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

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# デバック用途
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)