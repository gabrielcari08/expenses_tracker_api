from fastapi import FastAPI
from db.models import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
async def hello_fastapi():
    return {"message": "hello!"}