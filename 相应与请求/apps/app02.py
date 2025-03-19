from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

app02 = APIRouter()

class User(BaseModel):
    username: str
    password: str
    address: Optional[str] = None

@app02.post("/item",response_model=User, response_model_exclude={"password"})
async def login(item: User):
    print(item.model_dump())
    print(type(item))
    return item