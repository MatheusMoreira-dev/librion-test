from sqlalchemy.orm import Session
from infrastructure.repositories import BookRepository as r
from models import Book
from schemas import SearchBook
from utils import normalize_string

class BookService():

    @staticmethod
    def filter_books(session:Session, filters:SearchBook) -> list[Book]:
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