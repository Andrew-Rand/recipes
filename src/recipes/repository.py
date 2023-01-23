from typing import List
from uuid import UUID

from fastapi import HTTPException
from starlette import status

from src.base.repositories.base_repository import BaseRepository
from src.recipes.models import Recipe
from src.recipes.schemas import RecipeSchema


class RecipeRepository(BaseRepository):

    def create(self, recipe: RecipeSchema) -> Recipe:
        new_recipe = Recipe(
            title=recipe.title,
            short_description=recipe.short_description,
            description=recipe.description,
            comments=recipe.comments,
            link=recipe.link,
            file_links=recipe.file_links,
            user_id=str(recipe.user_id)
        )
        self.session.add(new_recipe)
        self.session.commit()
        self.session.refresh(new_recipe)
        return new_recipe

    def get_all(self) -> List[Recipe]:
        return self.session.query(Recipe).all()

    def get_all_for_user(self, user_id: UUID) -> Recipe:
        pass

    def get_by_id(self, _id: UUID) -> Recipe:
        if recipe := self.session.query(Recipe).get(_id):
            return recipe
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Object with given id does not exist')

    def update(self, _id: UUID, data: RecipeSchema) -> Recipe:
        # TODO: rewrite to avoid extra query
        if recipe := self.session.query(Recipe).get(_id):
            self.session.query(Recipe).filter(Recipe.id == _id).update(data.dict())
            self.session.commit()
            self.session.refresh(recipe)
            return recipe
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Object with given id does not exist')

    def delete(self, _id: UUID) -> None:
        # TODO rewrite with soft delete
        self.session.query(Recipe).filter(Recipe.id == _id).delete()
        self.session.commit()
