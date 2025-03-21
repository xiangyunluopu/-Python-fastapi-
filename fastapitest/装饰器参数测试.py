import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get(
    '/test',
    tags=['test tags'],
    summary='test summary',
    description='test description',
    response_description='test response',
    deprecated=True,
)
async def test():
    return {"test": "test"}

if __name__ == '__main__':
    uvicorn.run(
        '装饰器参数测试:app',
        port=8080,
        reload=True,
    )