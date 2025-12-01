from pydantic import BaseModel

class ReaderSchema(BaseModel):
    id_library: int
    name: str
    email: str
    password: str
    cep: str

    class Config:
        from_attributes = True
