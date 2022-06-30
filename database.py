#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Employee


URI = "mongodb+srv://threetiersystem:Xinyxo1DIUotsoEp@cluster0.ie2a2.mongodb.net/?retryWrites=true&w=majority"
# URI ='mongodb://localhost:27017/'

client = motor.motor_asyncio.AsyncIOMotorClient(URI)
database = client.face_db
collection = database.face


