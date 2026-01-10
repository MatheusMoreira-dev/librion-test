from sqlalchemy.orm import Session
from main import bcrypt_context
from infrastructure.repositories import LibraryRepository
from models import Library
from exceptions.library_exception import LibraryAlreadyExistsError

class LibraryService():

    # método para criar uma nova biblioteca
    @staticmethod
    def create(session: Session, new_library: Library):
        library = LibraryRepository.find_by_email(session, new_library.email)

        if library:
            raise LibraryAlreadyExistsError('Já existe uma biblioteca registrada com esse email!')
        
        # cria senha criptografada
        new_library.password = bcrypt_context.hash(new_library.password)

        # cria uma nova bibliotea
        LibraryRepository.create(session, new_library)

    # verifica por meio do email se um Library já está cadastrado 
    @staticmethod
    def already_registered(session: Session, email: str):
        library = LibraryRepository.find_by_email(session, email)
        
        return library
