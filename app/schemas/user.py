from pydantic import BaseModel, EmailStr, Field, PositiveInt

class UserBase(BaseModel):
    id: str
    username: str = Field(min_length=3, max_length=32)
    city: str
    age: PositiveInt
    email: EmailStr
    password: str = Field(min_length=5, max_length=32)