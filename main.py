# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path
from fastapi import Body

app = FastAPI()

# Models
class HairColor(str, Enum):
    RED = "red"
    BLOND = "blond"
    BROWN = "brown"
    BLACK = "black"

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="First Name",
        description="The person's first name"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="Last Name",
        description="The person's last name"
    )
    age: int = Field(
        ...,
        gt=0,
        lt=150,
        title="Age",
        description="The person's age"
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        title="Hair Color",
        description="The person's hair color"
    )
    is_married: Optional[bool] = Field(
        default=None,
        title="Is Married",
        description="Whether the person is married"
    )

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

@app.put('/person/{id}')
def update_person(
    id: int = Path(
        ...,
        ge=1,
        le=10,
        name='Id',
        description='The id of the person. It must be between 1 and 10'
    ),
    person: Person = Body(
        ...,
        name='Person',
        description='The person object.'
    ),
    location: Location = Body(
        ...,
        name='Location',
        description='The location object.'
    )
):
    data = {}
    data.update(person.dict())
    data.update(location.dict())

    return {'id': id, 'data': data}
