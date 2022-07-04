from fastapi import HTTPException, APIRouter, status
import face_recognition
import urllib.request
from app.model import Employee
from app.database import collection

router = APIRouter(
    prefix="/faces",
    tags=["Faces"]
)


@router.get("/")
async def get_employee_faces():
    faces = []
    cursor = collection.find({})
    async for document in cursor:
        faces.append(Employee(**document))
    return faces


@router.post("/", response_model=Employee)
async def post_employee_face(face: Employee):
    try:
        # open image url
        urllib.request.urlretrieve(
            face.photo,
            "temp.png")

        face_image = face_recognition.load_image_file("temp.png")

        face_locations = face_recognition.face_locations(face_image)

        if not face_locations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No face found in uploaded image")

        face_encoding = face_recognition.face_encodings(face_image)[0]

        face_embedding = face_encoding.tolist()

        document = {
            "first_name": face.first_name,
            "last_name": face.last_name,
            "email_address": face.email_address,
            "city": face.city,
            "id": face.id,
            "photo": face.photo,
            "phone_number": face.phone_number,
            "street_address": face.street_address,
            "embedding": face_embedding
        }
        response = await collection.insert_one(document)
        return document

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
