from fastapi import FastAPI, HTTPException, APIRouter
import face_recognition
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
    response = await create_face(face.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")




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
