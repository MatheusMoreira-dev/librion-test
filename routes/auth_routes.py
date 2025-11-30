from fastapi import APIRouter
from infrastructure.connectionDB import SessionLocal
from models import Library

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/create_library')
async def create_library(name: str, email: str, password: str, cep: str):
    with SessionLocal() as db:
        library = db.query(Library).filter(Library.email == email).first()
        if library:
            return {'mensagem': 'Já existe um usuário com esse email!'}
        else:
            new_library = Library(name, email, password, cep)
            db.add(new_library)
            db.commit()
            return {'mensagem': 'Usuário cadastrado com sucesso!'}
