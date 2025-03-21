from fastapi import APIRouter
user = APIRouter()

@user.get("/login")
async def login():
    return {"message": "login"}

@user.get('/register')
async def register():
    return {"message": "register"}
