from fastapi import FastAPI
from routers import auth, users
from db.models import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def hello_fastapi():
    return {"message": "hello!"}