import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from apps.test01 import test01
from apps.base_module_from import request_base_from
from apps.app01 import app01
from apps.app02 import app02

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(app02, tags=["相应模型测试"])
app.include_router(test01, tags=["路由测试"])
app.include_router(request_base_from, tags=["测试请求参数"])
app.include_router(app01,prefix="/file", tags=["文件上传测试"])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=False, workers=1)
