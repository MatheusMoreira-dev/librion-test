from sqlalchemy.orm import Session
from models import Copy, Loan

class LoanRepository:

    @staticmethod
    def register_loan(session: Session, loan: Loan):
        session.add(loan)
        session.commit()
        session.refresh(loan)

        return loan
    
    @staticmethod
    def find_loan_by_copy(session: Session, copy_id: int, reader_id: int):
        loan = session.query(Loan).filter(Loan.copy_id == copy_id, Loan.reader_id == reader_id).first()
        return loan

    @staticmethod
    def list_reader_loans(session:Session, reader_id:int):
        query = session.query(Loan).filter(Loan.reader_id == reader_id)
        
        return query.all()
    
    @staticmethod
    def list_library_loans(session:Session, library_id:id):
        query = session.query(Loan).join(Copy).filter(Copy.id_library == library_id)
        return query.all()
    
    @staticmethod
    def get_loan_by_id(session:Session, loan_id:int):
        query = session.query(Loan).filter(Loan.id == loan_id)

        return query.first()
    
    @staticmethod
    def register_taken_date(session:Session, loan_id:int):
        query = session.query(Loan).filter(Loan.id == loan_id).first()
        