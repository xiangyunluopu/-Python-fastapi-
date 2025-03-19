import os.path
from datetime import datetime
from typing import List

from fastapi import File, APIRouter, UploadFile

app01 = APIRouter()

@app01.post("/file")
async def file(file: bytes = File(...)):
    print(file)
    print(type(file))
    return {"file_len": len(file)}

@app01.post("/files")
async def files(files: List[bytes] = File(...)):
    file_len: List[int] = []
    for file in files:
        print(file)
        file_len.append(len(file))

    return {"files_len": file_len}

@app01.post("/uploadFile")
async def upload_file(file: UploadFile):
    path = os.path.join("files", file.filename)
    with open(path, "wb") as f:
        for line in iter(file.file.readline, b""):
            f.write(line)
        f.close()
    print(file.filename)
    print(type(file))
    return {"filename": file.filename}


@app01.post("/uploadFiles")
async def upload_files(files: List[UploadFile]):
    filenames: List[str] = []
    for file in files:
        filenames.append(file.filename)
        path = os.path.join("files", filenames[-1])
        with open(path, "wb") as f:
            for line in iter(file.file.readline, b""):
                f.write(line)
            f.close()
    return {"filenames": filenames}