from typing import Annotated
import cv2
import os

import PIL

from temp import *

from PIL import Image

from check_status import *

from fastapi import FastAPI,Path,Query,Form,File,UploadFile

app=FastAPI()

from process_initialisation import *


@app.get("/upload_file/{}")





@app.get("/upload_file/{image_file_name}")
async def check_status(image_file_name:str):
    pres_status=present_status(image_file_name)

    return{"present status":pres_status}



#@app.post("/login/")
#async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
 #   return {"username":username}

#@app.post("/uploadfile/")
#async def create_upload_file(file:UploadFile):
#    contents=await file.read()
#    return {contents}
#


@app.post("/upload_file/{image_file_name}")
async def start_process(image_file_name:str):

    initialise(image_file_name)








@app.post("/upload_file")
async def send_image(image_file:UploadFile):
    contents=await image_file.read()
    
    if not os.path.isdir("Uploaded_Images"):
        os.makedirs("Uploaded_Images")
    


    with open(os.path.join("Uploaded_Images", image_file.filename), "wb") as f:
        f.write(contents)


    # meta_integrate(contents)
    add_file_path(os.path.join("Uploaded_Images",image_file.filename));
    

    return {"filename":image_file.filename}
    

    

