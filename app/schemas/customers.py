from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
