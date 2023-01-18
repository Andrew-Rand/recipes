from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.base.models import BaseModel


class Recipe(BaseModel):
    __tablename__ = 'recipes'

    title = Column(String(100))
    short_description = Column(String(500))
    description = Column(String)
    comments = Column(String(1000))
    link = Column(String)
    file_links = Column(ARRAY(item_type=String, as_tuple=False, dimensions=None, zero_indexes=True))
    # user =