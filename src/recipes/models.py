from typing import Any, Dict

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship, backref

from src.base.models import BaseModel
from src.user.models import User


class Recipe(BaseModel):
    __tablename__ = 'recipes'

    title = Column(String(100))
    short_description = Column(String(500))
    description = Column(String)
    comments = Column(String(1000))
    link = Column(String)
    file_links = Column(ARRAY(item_type=String, as_tuple=False, dimensions=None, zero_indexes=True))

    user_id = Column(UUID, ForeignKey(User.id))
    user = relationship(User, backref=backref("saved_recipes", lazy="dynamic"))
