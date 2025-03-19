import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.student_api import student_api
from config.config import TORTOISE_ORM

app = FastAPI()

register_tortoise(app, config=TORTOISE_ORM)

app.include_router(student_api, prefix='/student', tags=["学生业务接口"])




if __name__ == '__main__':
    uvicorn.run(app, port=8000)