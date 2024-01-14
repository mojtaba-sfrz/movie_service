from sqlalchemy import (Table, Column, MetaData,
                        create_engine, Integer, String, ARRAY)

from databases import Database

import os

DATABASE_URL = os.getenv("MOVIE_DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('cast_id', ARRAY(Integer)),
)

database = Database(DATABASE_URL)
