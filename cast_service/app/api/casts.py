from fastapi import APIRouter, HTTPException

from app.api.models import CastIn, CastOut, CastUpdate

from app.api import db_manager

casts = APIRouter()


@casts.get('/{id}', response_model=CastOut)
async def get_cast(id:int):

    cast = await db_manager.get_cast(id)

    if not cast:
        raise HTTPException(status_code=404, detail="cast not found")
    
    return cast


@casts.post('/', response_model=CastOut, status_code=201)
async def add_cast(playload:CastIn):
    cast_id = await db_manager.add_cast(playload)

    responce = {
        'id': cast_id,
        **playload.dict(),
    }

    return responce