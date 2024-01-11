from app.api.db import database, engine, metadata
from fastapi import FastAPI
from app.api.movies import movies


metadata.creat_all(engine)

app= FastAPI

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shtdown():
    await database.disconnect()

app.include_router(movies)