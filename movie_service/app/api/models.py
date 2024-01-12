from typing import List, Optional
from pydantic import BaseModel

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):

    name: Optional[str] = None
    plot: optional[str] = None
    genres: optional[str] = None
    casts: Optional[str] = None

