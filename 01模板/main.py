from functools import lru_cache

import uvicorn
from fastapi import FastAPI, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates


@lru_cache()
def get_templates():
    print("Initializing Jinja2Templates")
    return Jinja2Templates(directory="templates")


app = FastAPI()


@app.get("/index")
async def index(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    user = {"username": "root", "age": 12}
    books = ["金瓶梅", "聊斋", "国色天香", "剪灯新话"]
    movies = {
        "adult_movie": ["欧美", "日韩"],
        "juvenile_movie": ["黑猫警长", "成龙历险记"]
    }
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "user": user,
            "books": books,
            "Pai": 3.14,
            "movies": movies,
        }
    )


if __name__ == '__main__':
    uvicorn.run(app, port=8000)