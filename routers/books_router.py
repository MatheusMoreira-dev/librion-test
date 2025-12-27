from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.dependencies import get_session
from sqlalchemy.orm import Session
from services import BookService
from schemas import SearchBook
from exceptions.book_exception import BookNotFound

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/")
async def get_books(
    cursor:int = Query(1, ge=1), 
    size:int = Query(10, le=50), 
    session:Session = Depends(get_session)
    ):

    """Get books limit by cursor and size"""
    return BookService.list_books(cursor, size, session)

@books_router.post("/search")
async def filter_books(filters:SearchBook, session:Session = Depends(get_session)):
    """Search using a combination of filters."""
    return BookService.filter_books(session, filters)

@books_router.get("/{id}")
async def get_book_by_id(id:int, session:Session = Depends(get_session)):
    try:
        return BookService.get_by_id(id, session)

    except BookNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception:
        raise HTTPException(status_code=500)

@books_router.get("/{id}/copies")
def get_copies():
    pass