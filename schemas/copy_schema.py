from pydantic import BaseModel
from schemas.library_schema import LibraryResponse
from schemas.book_schema import BookSchema

class CopyBase(BaseModel):
    quantity: int
    #quantity_available:int
    is_global: bool

    class Config:
        from_attributes = True
    
class CopyCreate(CopyBase):
    isbn: str

    class Config:
        from_attributes = True

class CopyResponse(CopyBase):
    library:LibraryResponse
    book: BookSchema
    
    class Config:
        from_attributes = True