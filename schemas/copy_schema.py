from pydantic import BaseModel

class CopySchema(BaseModel):
    id_library: int
    isbn: str
    quantity: int
    is_global: bool
    
    class Config:
        from_attributes = True