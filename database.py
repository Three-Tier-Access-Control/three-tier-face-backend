#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Face

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.FaceList
collection = database.face


