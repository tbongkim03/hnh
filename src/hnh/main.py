from typing import Union
from fastapi import Request
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates


app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):    
    return {"file_name": file.filename}

@app.get("/predict_hotdog")
def predict_hotdog():
    from random import choice
    result = choice(["hotdog", "not hotdog"])
    return {"result": result}