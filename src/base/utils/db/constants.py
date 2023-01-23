import os

from sqlalchemy.orm import declarative_base

# DB_USER = os.environ.get("POSTGRES_USER")
# DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
# DB_HOST = os.environ.get("POSTGRES_HOST")
# DB_PORT = os.environ.get("POSTGRES_PORT")
# DB_DATABASE = os.environ.get("POSTGRES_DB")

DB_USER = 'test'
DB_PASSWORD = 'password'
DB_HOST = '127.0.0.1'
DB_PORT = 5432
DB_DATABASE = 'test-db'

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

Base = declarative_base()
