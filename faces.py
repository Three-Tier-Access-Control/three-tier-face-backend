from fastapi import HTTPException, APIRouter, status
import face_recognition
import urllib.request
from model import Face
from database import (
    fetch_all_faces,
    create_face
)

router = APIRouter(
    prefix="/faces",
    tags=["faces"]
)


@router.get("/")
async def get_face():
    response = await fetch_all_faces()
    return response


@router.post("/", response_model=Face)
async def post_face(face: Face):
    # open image url 
    urllib.request.urlretrieve(
        face.photo,
        "temp.png")

    face_image = face_recognition.load_image_file("temp.png")

    face_locations = face_recognition.face_locations(face_image)

    if face_locations:
        face_encoding = face_recognition.face_encodings(face_image)[0]

        face_embedding = face_encoding.tolist()

        response = await create_face({
            "first_name": face.first_name,
            "last_name": face.last_name,
            "email_address": face.email_address,
            "city": face.city,
            "id": face.id,
            "photo": face.photo,
            "phone_number": face.phone_number,
            "street_address": face.street_address,
            "embedding": face_embedding
        })
        if response:
            return response
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No face found in uploaded image")
