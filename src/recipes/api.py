from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.recipes.models import Recipe
from src.recipes.repository import RecipeRepository
from src.recipes.schemas import RecipeSchema, RecipeResponseSchema, RecipeUpdateSchema
from src.base.utils.db.engine import get_db


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RecipeResponseSchema)
async def add_recipe(recipe: RecipeSchema, db: Session = Depends(get_db)) -> RecipeSchema:
    repo = RecipeRepository(db)
    return repo.create(recipe)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[RecipeResponseSchema])
async def get_all(db: Session = Depends(get_db)) -> List[RecipeSchema]:
    # TODO: rewrite with filter by user id from header
    repo = RecipeRepository(db)
    return repo.get_all()


@router.get('/{id}/', status_code=status.HTTP_200_OK, response_model=RecipeResponseSchema)
async def get_by_id(_id: UUID,  db: Session = Depends(get_db)) -> RecipeSchema:
    repo = RecipeRepository(db)
    return repo.get_by_id(_id)


@router.put('/{id}/', status_code=status.HTTP_202_ACCEPTED, response_model=RecipeResponseSchema)
async def update(_id: UUID, recipe: RecipeUpdateSchema, db: Session = Depends(get_db)) -> RecipeSchema:
    repo = RecipeRepository(db)
    return repo.update(_id, recipe)


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def update(_id: UUID, db: Session = Depends(get_db)) -> None:
    repo = RecipeRepository(db)
    repo.delete(_id)

