from fastapi import APIRouter, Depends, UploadFile, File, status, HTTPException
from slugify import slugify
from .models import Category
from .pydentic_models import categoryitem
import os
import datetime

router = APIRouter()


@router.post("/category/")
async def create_category(data: categoryitem = Depends(),
                          category_image: UploadFile = File(...)):
    if await Category.exists(name=data.name):
        return {"status": False, "message": "cartegory already exists"}
    else:
        slug = slugify(data.name)
        FILEPATH = "static/"

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png", "jpg", "jpeg",]:
            return {"status": "error", "detail": "file extension not allowed"}

        dt = datetime.time()

        modefied_image_name = imagename+"_"+str(dt)+"."+extension
        generated_name = FILEPATH+modefied_image_name
        file_content = await category_image.read()

        with open(generated_name, "wb") as file:
            file.write(file_content)

            file.close()

        # image_url=app_url+generated_name

        category_obj = await Category.create(
            category_image=generated_name,
            description=data.description,
            name=data.name,
            slug=slug
        )







@router.post("/Subcategory/")
async def create_Subcategory(data: categoryitem = Depends(),
                          category_image: UploadFile = File(...)):
    if await Category.exists(name=data.name):
        return {"status": False, "message": "cartegory already exists"}
    else:
        slug = slugify(data.name)
        FILEPATH = "static/"

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png", "jpg", "jpeg",]:
            return {"status": "error", "detail": "file extension not allowed"}

        dt = datetime.time()

        modefied_image_name = imagename+"_"+str(dt)+"."+extension
        generated_name = FILEPATH+modefied_image_name
        file_content = await category_image.read()

        with open(generated_name, "wb") as file:
            file.write(file_content)

            file.close()

        # image_url=app_url+generated_name

        category_obj = await Category.create(
            category_image=generated_name,
            description=data.description,
            name=data.name,
            slug=slug
        )