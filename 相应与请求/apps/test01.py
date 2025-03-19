from fastapi import APIRouter

test01 = APIRouter()


@test01.get("/test")
async def index():
    return {"message": "Hello World"}