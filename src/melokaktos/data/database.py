# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///melokaktos.db"

engine = create_engine(DATABASE_URL, echo=True)
# TO-DO: make sure to change to the following code before shipping
# engine = create_engine(DATABASE_URL, echo=os.getenv("MELOKAKTOS_DEBUG") == "1")

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
