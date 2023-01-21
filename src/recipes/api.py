from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.recipes.models import Recipe
from src.recipes.schemas import RecipeSchema
from src.utils.db.engine import get_db

router = APIRouter()


@router.post('/')
async def add_recipe(recipe: RecipeSchema, db: Session = Depends(get_db)):
    new_recipe = Recipe(
        title=recipe.title,
        short_description=recipe.short_description,
        description=recipe.description,
        comments=recipe.comments,
        link=recipe.link,
        file_links=recipe.file_links,
        user_id=str(recipe.user_id)
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe
