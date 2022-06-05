#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Face

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.FaceList
collection = database.face

async def fetch_one_face(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_faces():
    faces = []
    cursor = collection.find({})
    async for document in cursor:
        faces.append(Face(**document))
    return faces

async def create_face(face):
    document = face
    result = await collection.insert_one(document)
    return document


async def update_face(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_face(title):
    await collection.delete_one({"title": title})
    return True