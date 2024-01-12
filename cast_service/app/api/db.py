from sqlalchemy import (Table, Column, creat_engine,
                        MetaData, String, Integer)

from databases import Database

import os 



DATABASE_URL = os.getenv("CAST_DATABASE_URL")

engine = creat_engine(DATABASE_URL)

metadata = MetaData()

casts = Table(
    "casts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("nationality", String(50))
)

database = Database(DATABASE_URL)