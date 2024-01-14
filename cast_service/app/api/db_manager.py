from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database


async def get_cast(id: int):

    query = casts.select(casts.c.cast_id == id)

    return await database.execute(query=query)


async def add_cast(playload: CastIn):

    query = casts.insert().values(**playload.dict())

    return await database.execute(query=query)
