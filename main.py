from fastapi import FastAPI

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

