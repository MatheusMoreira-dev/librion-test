from sqlalchemy.orm import Session
from models import Copy

# repositório de exemplar
class CopyRepository():

    @staticmethod
    def create(session: Session, copy: Copy):
        session.add(copy)
        session.commit()
