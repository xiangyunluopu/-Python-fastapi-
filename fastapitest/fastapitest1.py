import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/shop")
async def shop():
    return {"message": "..."}

if __name__ == '__main__':
    uvicorn.run('fastapitest1:app', port=8089, reload=True)
