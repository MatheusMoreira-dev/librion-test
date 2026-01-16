from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from infrastructure.connectionDB import Base
from .user import User

# classe de bibliotecas
class Library(User, Base):
    
    __tablename__ = 'library'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    cep = Column('cep', String, nullable=False)
    admin = Column('admin', Boolean, default=False, nullable=False)

    copies = relationship('Copy', back_populates='library')

    def __init__(self, name: str, email: str, password: str, cep: str):
        super().__init__(name, email, password, cep)
        self.admin = True
