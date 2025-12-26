from sqlalchemy.orm import Session
from sqlalchemy import select, exists
from models import Book, Copy
from schemas import SearchBook

# repositório de um livro
class BookRepository():

    @staticmethod
    def based_query(session: Session):
        return session.query(Book)
    
    @staticmethod
    def join_book_copies(query):
        return query.join(Copy)

    @staticmethod
    def create(session: Session, book: Book):
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

    @staticmethod
    def find_by_isbn(session: Session, isbn: str):
        book = session.query(Book).filter(Book.isbn == isbn).first()
        return book
    
    @staticmethod
    def all_books(session:Session):
        return session.query(Book).all()
    
    @staticmethod
    def filter_by_title(query, title:str|None):
        if not title or title == "":
            return query
        
        return query.where(Book.search_title.contains(title))
        
    @staticmethod
    def filter_by_categories(query, category_ids:list[int]|None):
        if not category_ids:
            return query
        
        return query.where(Book.id_category.in_(category_ids))
    
    @staticmethod
    def filter_by_libraries(query, library_ids:list[int]|None):
        if not library_ids:
            return query

        return query.where(Copy.id_library.in_(library_ids))
    
    @staticmethod
    def availables(query):
        return query.where(
            exists().where(
                (Copy.id_library == Book.id) &
                (Copy.quantity > 0)
            )
        )