from sqlalchemy.orm import Session
from infrastructure.repositories import BookRepository as r
from schemas import SearchBook
from utils import normalize_string
from exceptions.book_exception import BookNotFound

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
        return r.combined_filters(session, filters)
    
    @staticmethod
    def get_by_id(book_id:int, session:Session):
        book = r.get_by_id(session, book_id)

        if not book:
            raise BookNotFound()

        return book
    
    @staticmethod
    def get_copies(book_id:int, session:Session):
        #Verifica se existe um livro com esse Id
        BookService.get_by_id(book_id, session)

        return r.list_copies(session, book_id)