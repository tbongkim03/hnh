from typing import Union
from fastapi import Request
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates

from random import choice
from transformers import pipeline

app = FastAPI()

html = Jinja2Templates(directory="public")


@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    from PIL import Image
    img = Image.open(io.BytesIO(img)) # 이미지를 PIL dlalwlfh qusghks
    predictions = model(img)
    return {"Hello": file.filename}

@app.get("/predict_hotdog")
def predict_hotdog():
    result = choice(["hotdog", "not hotdog"])
    return {"result": result}