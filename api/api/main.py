from fastapi import FastAPI, Response

from .database import SessionLocal, engine


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World?"}
