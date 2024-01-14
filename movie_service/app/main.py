from app.api.db import database, engine, metadata
from fastapi import FastAPI
from app.api.movies import movies
import asyncio


app = FastAPI(openapi_url="/api/v1/movies/openapi.json",
              docs_url="/api/v1/movies/docs")

metadata.create_all(engine)


async def connect_to_database():
    retries = 0
    while retries < 5:
        try:
            await database.connect()
            break
        except Exception as e:
            print(
                f"Failed to connect to the database. Retrying... ({retries + 1}/5)")
            await asyncio.sleep(2)
            retries += 1
    else:
        print("Max retries reached. Exiting.")
        raise SystemExit(1)


@app.on_event("startup")
async def startup():
    await connect_to_database()


@app.on_event("shutdown")
async def shtdown():
    await database.disconnect()

app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])
