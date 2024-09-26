from typing import Union

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    return {"file_name": file.filename}

@app.get("/predict_hotdog")
def predict_hotdog():
    from random import choice
    result = choice(["hotdog", "not hotdog"])
    return {"result": result}