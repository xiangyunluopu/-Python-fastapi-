import uvicorn
from fastapi import FastAPI
from apps.user import user
from apps.shop import shop

app = FastAPI()

app.include_router(user,prefix="/user", tags=["user tags"])
app.include_router(shop,prefix="/shop", tags=["shop tags"])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)