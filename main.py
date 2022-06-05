from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Face
from database import (
    fetch_one_face,
    fetch_all_faces,
    create_face,
    update_face,
    remove_face,
)

# an HTTP-specific exception class  to generate exception information

app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/face")
async def get_face():
    response = await fetch_all_faces()
    return response

@app.get("/api/face/{title}", response_model=Face)
async def get_face_by_title(title):
    response = await fetch_one_face(title)
    if response:
        return response
    raise HTTPException(404, f"There is no face with the title {title}")

@app.post("/api/face/", response_model=Face)
async def post_face(face: Face):
    response = await create_face(face.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/face/{title}/", response_model=Face)
async def put_face(title: str, desc: str):
    response = await update_face(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no face with the title {title}")

@app.delete("/api/face/{title}")
async def delete_face(title):
    response = await remove_face(title)
    if response:
        return "Successfully deleted face"
    raise HTTPException(404, f"There is no face with the title {title}")