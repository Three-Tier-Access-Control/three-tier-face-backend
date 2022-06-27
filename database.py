#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Employee

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.face_db
collection = database.face


