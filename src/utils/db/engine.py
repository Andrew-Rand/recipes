from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.utils.db.constants import DB_URL


engine = create_engine(DB_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
