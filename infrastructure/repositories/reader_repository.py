from sqlalchemy.orm import Session
from models import Reader

# repositório de leitores
class ReaderRepository():

    @staticmethod
    def create(session: Session, reader: Reader):
        session.add(reader)
        session.commit()
    
    @staticmethod
    def find_by_email(session: Session, email: str):
        reader = session.query(Reader).filter(Reader.email == email).first()
        return reader
