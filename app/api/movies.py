from typing import List

from fastapi import Header, APIRouter

from app.api.models import Movie

movies = APIRouter

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


@movies.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db

@movies.post('/', status_code=201)
async def add_movie(playload:Movie):
    movie = playload.dict()
    fake_movie_db.append(movie)
    return {id:len(fake_movie_db)-1}

@movies.put('/{id}')
async def update_movie(id: int, playload:Movie):
    movie = playload.dict()
    movie_len = len(fake_movie_db)

    if 0 <= id <= movie_len :
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Move not found")

@movies.delete('/{id}')
async def delete_movie(id:int):
    movie_len = len(fake_movie_db)

    if 0 <= id <= movie_len :
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail="Move not found")
