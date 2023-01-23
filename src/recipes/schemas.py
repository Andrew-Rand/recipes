from typing import List
from uuid import UUID

from pydantic import BaseModel


class RecipeSchema(BaseModel):
    title: str
    short_description: str = None
    description: str = None
    comments: str = None
    link: str = None
    file_links: List[str] = None
    user_id: UUID


class RecipeResponseSchema(RecipeSchema):

    class Config:
        orm_mode = True


class RecipeUpdateSchema(RecipeSchema):
    class Config:
        fields = {'user_id': {'exclude': True}}
