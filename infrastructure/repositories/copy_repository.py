from sqlalchemy.orm import Session, joinedload
from models import Copy

# repositório de exemplar
class CopyRepository():

    @staticmethod
    def create(session: Session, copy: Copy):
        session.add(copy)
        session.commit()

    @staticmethod
    def get_all(session: Session, id_library: int):
        all_copies = session.query(Copy).options(joinedload(Copy.book)).filter(Copy.id_library == id_library).all()
        return all_copies