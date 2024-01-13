from fastapi import FastAPI
from app.api.db import metadata, engine, database
from app.api.casts import casts

app = FastAPI

metadata.creat_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()


app.on_event("shutdown")
async def shtdown():
    await database.disconnect()




app.inclide_router(casts, prefix='/api/v1/casts', tags=['casts'])
