from sqlalchemy.orm import Session
from infrastructure.repositories import BookRepository as r
from models import Book
from schemas import SearchBook
from utils import normalize_string

class BookService():

    @staticmethod
    def list_books(cursor:int|None, size:int, session:Session):
        books = r.list_books(cursor, size, session)
        next_cursor = books[-1].id if books else None 
        
        return {
            "books": books,
            "next_cursor": next_cursor
        }

    @staticmethod
    def filter_books(filters:SearchBook, session:Session):
        query = r.based_query(session)

        if filters.title:
            query = r.filter_by_title(query, normalize_string(filters.title))
        
        if filters.category_ids:
            query = r.filter_by_categories(query, filters.category_ids)

        if filters.available:
            query = r.availables(query)
        
        if filters.library_ids:
            query = r.join_book_copies(query)
            query = r.filter_by_libraries(query, filters.library_ids)

        return session.execute(query).scalars().all()
    
    @staticmethod
    def get_by_id(id:int, session:Session):
        return r.get_by_id(session, id)