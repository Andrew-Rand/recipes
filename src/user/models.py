from sqlalchemy import Column, String, Boolean, Integer

from src.base.models import BaseModel


class User(BaseModel):

    __tablename__ = 'users'

    username = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(200))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
