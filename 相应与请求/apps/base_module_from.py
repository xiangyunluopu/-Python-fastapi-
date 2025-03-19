from typing import Optional

from fastapi import APIRouter
from fastapi import Form
from pydantic import BaseModel


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    name: Optional[str]
    age: Optional[int]
    password: Optional[str]
    address: Optional[Addr]


request_base_from = APIRouter()


@request_base_from.post("/user/register")
async def register(user: User):
    print(user, type(user))
    print(user.model_dump())
    return user


@request_base_from.post("/user/login")
async def login(username: str = Form(...), password: str = Form(...)):
    print(username, type(username))
    print(username, type(username))
    return {"username": username, "password": password}
