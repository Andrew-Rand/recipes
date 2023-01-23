from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.base.utils.db.constants import DB_URL


engine = create_engine(DB_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
