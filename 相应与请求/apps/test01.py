from fastapi import APIRouter

test01 = APIRouter()


@test01.get("/")
async def index():
    return {"message": "Hello World"}