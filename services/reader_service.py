from sqlalchemy.orm import Session
from main import bcrypt_context
from infrastructure.repositories import ReaderRepository as r
from models import Reader
from exceptions.reader_exception import ReaderAlreadyExistsError

class ReaderService():

    # método para cirar um novo leitor
    @staticmethod
    def create(session: Session, new_reader: Reader):
        reader = r.find_by_email(session, new_reader.email)

        if reader:
            raise ReaderAlreadyExistsError('Já existe um usuário cadastrado com esse email')
        
        # cria senha criptografada
        new_reader.password = bcrypt_context.hash(new_reader.password)

        # cria um novo leitor
        r.create(session, new_reader)
