from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/{param}")
async def root(
        param,
        param1: Optional[str] = None,
        param2: Optional[str] = None,
        param3: Optional[str] = None
):
    if param1 is None: param1 = " "
    if param2 is None: param2 = " "
    if param3 is None: param3 = " "
    return {
        "message": param + "/" + param1 + "/" + param2 + "/" + param3
    }


if __name__ == '__main__':
    uvicorn.run("request_parameter_test:app", reload=True)
