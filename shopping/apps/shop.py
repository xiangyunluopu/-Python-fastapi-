from fastapi import APIRouter

shop = APIRouter()

@shop.get('bed')
async def bed():
    return {'message': 'bed'}

@shop.get('book')
async def book():
    return {'message': 'book'}