from sqlalchemy.orm import Session
from models import Book

# repositório de um livro
class BookRepository():

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
