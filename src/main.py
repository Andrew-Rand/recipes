from typing import List

from fastapi import FastAPI, Query, Path

app = FastAPI()
















#  ----------------------------------------------------
# demo FastAPI functionality tutorial
#  ---------------------------------------------------

@app.get('/hello')
def hello():
    return {'hello': 'world'}


# models and validation
from pydantic import BaseModel, validator, Field


class Category(BaseModel):
    id: int
    name: str


class Item(BaseModel):
    title: str
    description: str = None
    categories: List[Category] = None
    number: int = None
    validated_field: int = Field(None, ge=10, le=100, exclude=(1, 2, 3))  # validator variant 1

    @validator('number')  # validator variant 2 (rise ValueError)
    def check_number(cls, value):
        check_list = [5, 10, 25]
        if value not in check_list:
            raise ValueError(f'Use value from {check_list}')


# handlers
@app.post('/test_get/{pk}/')
def get_item(
        item: Item,  # use this model in request body (always first argument)
        pk: int = Path(..., gt=1, lt=10),  # ad pk after url (you can use just pk: int)
        query_param: str = Query(None, min_length=2, max_length=5)  # to provide query_param value use ?query_param=hi?

):
    return {'pk': pk, 'query_param': query_param, 'item': item}
