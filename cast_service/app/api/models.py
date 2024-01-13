from pydantic import BaseModel
from typing import Optional

class CastIn(BaseModel):
    
    name : str
    nationality : optional(str) = None


class CastOut(CastIn):

    id : int


class CastUpdate(BaseModel):

    name : opstional(str) = None
    