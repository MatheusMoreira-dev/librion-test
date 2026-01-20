from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str
    admin: bool = False

    class Config:
        from_attributes = True
