from fastapi import FastAPI, HTTPException, APIRouter
import face_recognition
import urllib.request
from PIL import Image
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
    urllib.request.urlretrieve(
    face.photo,
    "temp.png")
    
    face_image = face_recognition.load_image_file("temp.png")

    face_locations = face_recognition.face_locations(face_image)

    print(face_locations)

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
    raise HTTPException(500, "Something went wrong")




# def encode_face():
#     # Load a sample picture and learn how to recognize it.
#     face_image = face_recognition.load_image_file(
#         "face-recognition/known_faces/Ashley_Shumba_0003.png")

#     face_encoding = face_recognition.face_encodings(face_image)[0]

#     faces.insert_one(
#         {
#             "first_name": "Ashley",
#             "last_name": "Shumba",
#             "email_address": "ashleytshumba@gmail.com",
#             "role": "Developer",
#             "national_id": "58-303326E67",
#             "city": "Bulawayo",
#             "is_active": True,
#             "id": "99201631-f60f-42fc-8e1c-8c5f72c3ec22",
#             "profile_image": "",
#             "phone_number": "0787382522",
#             "street_address": "14654 Inungu Rd, Selborne Park",
#             "embedding": face_encoding
#         },
#     )
