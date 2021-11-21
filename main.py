# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get('/')
def home():
    return {'message': 'Hello FastAPI World'}

@app.post('/person')
def create_person(person: Person = Body(...)):
    return person

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        name='Name',
        description='The name of the person. It must be between 1 and 50',
    ),
    age: int = Query(
        ...,
        ge=18,
        name='Age',
        description='The age of the person. Only accepts over 18 years old'
    )
):
    return {name: age}

@app.get('/person/{id}')
def show_person_by_id(
    id: int = Path(
        ...,
        ge=1,
        le=10,
        name='Id',
        description='The id of the person. It must be between 1 and 10'
    )
):
    return {'id': id}
