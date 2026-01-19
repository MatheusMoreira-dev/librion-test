from pydantic import BaseModel, field_validator
from pydantic_core import PydanticUndefined

class ReaderBase(BaseModel):
    name: str
    email: str
    cep: str

    class Config:
        from_attributes = True

class ReaderCreate(ReaderBase):
    password: str

    class Config:
        from_attributes = True
    
class ReaderUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    cep: str | None = None

    @field_validator('name', 'email', 'cep', mode='before')
    @classmethod 
    def ignore_empty_or_null(cls, value):
        if value is None:
            return PydanticUndefined
        if isinstance(value, str) and not value.strip():
            return PydanticUndefined
        return value

    class Config:
        from_attributes = True

class ReaderResponse(ReaderBase):
    id: int
    id_library: int

    class Config:
        from_attributes = True
