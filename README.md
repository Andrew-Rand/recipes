# recipes


### install dependencies

````
pip install pipenv
pipenv install 
````

### run application with uvicorn

````
uvicorn src.main:app --port 8000 --reload
````


### demo endpoint:

[/hello](http://127.0.0.1:8000/hello)

````
{"hello":"world"}
````

### App documentation
* [/docs](http://127.0.0.1:8000/docs) - swagger
* [/redoc](http://127.0.0.1:8000/redoc) - fastAPI auto docs


### Alembic migration

To update migration with alembic use command

````
alembic revision --autogenerate -m "First Migration"
````

To apply migration in db use command

````
alembic upgrade head
````