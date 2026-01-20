from pydantic import BaseModel
from schemas.library_schema import LibraryResponse
from schemas.book_schema import BookResponse

class CopyBase(BaseModel):
    quantity: int
    is_global: bool

    class Config:
        from_attributes = True
    
class CopyCreate(CopyBase):
    isbn: str

    class Config:
        from_attributes = True

class CopyResponse(CopyBase):
    id: int
    library:LibraryResponse
    book: BookResponse
    quantity_available: int
    
    class Config:
        from_attributes = True
        