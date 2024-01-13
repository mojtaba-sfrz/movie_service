from aqlalchemy import (Table, Column, MetaData,
                         creat_engine, Integer, String, ARRAY)

from dataclasses import Database

import os

DATABASE_URL = os.getenv("MOVIE_DATABASE_URL")

engine = creat_engine(DATABASE_URL)
metadat = MetaData()

movies = Table(
    "movies",
    metadat,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('cast_id', ARRAY(Integer)),
)

database = Database(DATABASE_URL)