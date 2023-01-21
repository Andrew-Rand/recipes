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
