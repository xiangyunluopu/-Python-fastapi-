import uvicorn
from fastapi import FastAPI
from apps.test01 import test01

app = FastAPI()

app.include_router(test01, tags=["路由测试"])


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)

