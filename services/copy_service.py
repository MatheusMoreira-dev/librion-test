from sqlalchemy.orm import Session
from infrastructure.repositories import CopyRepository, BookRepository, ReaderRepository
from models import Copy, Book
from exceptions.copy_exception import IsbnNotFoundError, CopyNotFoundError, CopyNotAvailableError, LoanOfCopyDenied
from exceptions.reader_exception import ReaderNotFoundError
from utils import search_book
from schemas import CopyCreate, LoanRequest

class CopyService():

    @staticmethod
    def create(session: Session, data_copy:CopyCreate, library_id:int):
        book = BookRepository.find_by_isbn(session, data_copy.isbn)

        if book:
            copy = Copy(**data_copy.model_dump(exclude={"isbn"}), id_library = library_id, id_book = book.id)
            return CopyRepository.create(session, copy)
        else: 
            try:
                book_data = search_book(data_copy.isbn)
                book = Book(**book_data.model_dump())
                book = BookRepository.create(session, book)
                copy = Copy(**data_copy.model_dump(exclude={"isbn"}), id_library = library_id, id_book = book.id)
                return CopyRepository.create(session, copy)
                
            except IsbnNotFoundError as e:
                raise IsbnNotFoundError(str(e))
            
    @staticmethod
    def get_all(session: Session, id_library: int):
        all_copies = CopyRepository.get_all(session, id_library)
        return all_copies
    
    @staticmethod
    def loan_copy(data_request: LoanRequest, session: Session):
        # Busca o exemplar no banco de dados
        copy = CopyRepository.find_copy(session, data_request.copy_id)

        # Erro: O exemplar não foi encontrado
        if not copy:
            raise CopyNotFoundError(str("Exemplar não encontrado!"))
        
        # Busca o leitor no banco de dados
        reader = ReaderRepository.find_reader_by_id(session, data_request.reader_id)

        # Erro: O leitor não foi encontrado
        if not reader:
            raise ReaderNotFoundError(str("Leitor não encontrado"))

        # Erro: Não há exemplar disponível
        if copy.quantity_available == 0:
            raise CopyNotAvailableError(str("Exemplar indisponível para empréstimo!"))
        
        # Erro: O livro não é global e não pertence a biblioteca de origem do leitor
        if not copy.is_global and copy.id_library != reader.id_library:
            raise LoanOfCopyDenied(str("O usuário não tem permissão de solicitar o empréstimo desse exemplar"))
        
        
