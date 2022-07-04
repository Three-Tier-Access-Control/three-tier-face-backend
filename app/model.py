from typing import Optional
from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    id: str
    first_name: str
    last_name: str
    email_address: EmailStr
    photo: str
    phone_number: str
    city: Optional[str] = None
    street_address: Optional[str] = None
    embedding: Optional[list] = []


