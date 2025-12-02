from sqlalchemy.orm import Session
from infrastructure.repositories import CopyRepository, BookRepository
from models import Copy, Book
from exceptions.copy_exception import IsbnNotFoundError
from utils import find_book

class CopyService():

    @staticmethod
    def create(session: Session, id_library: int, isbn: str, quantity: int, is_global: bool):
        book = BookRepository.find_by_isbn(session, isbn)

        if book:
            copy = Copy(id_library, book.id, quantity, is_global)
            CopyRepository.create(session, copy)
        else: 
            try:
                book_data = find_book(isbn)
                title = book_data['title']
                author = book_data['author']
                descrption = book_data['description']
                image = book_data['image']
                age_rating = book_data['age_rating']
                book = Book(1, title, author, descrption, image, age_rating, isbn)
                book = BookRepository.create(session, book)
                copy = Copy(id_library, book.id, quantity, is_global)
                CopyRepository.create(session, copy)
                
            except IsbnNotFoundError as e:
                raise IsbnNotFoundError(str(e))
            
    @staticmethod
    def get_all(session: Session, id_library: int):
        all_copies = CopyRepository.get_all(session, id_library)
        return all_copies
