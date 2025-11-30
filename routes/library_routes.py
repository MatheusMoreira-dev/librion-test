from fastapi import APIRouter
from infrastructure.connectionDB import SessionLocal
from models import Reader

library_router = APIRouter(prefix='/library', tags=['library'])

@library_router.post('/create_reader')
async def create_reader(id_library: int, name: str, email: str, password: str, cep: str):
    with SessionLocal() as db:
        reader = db.query(Reader).filter(Reader.email == email).first()
        if reader:
            return {'mensagem': 'Já existe um usuário com esse email!'}
        else:
            new_reader = Reader(id_library, name, email, password, cep)
            db.add(new_reader)
            db.commit()
            db.query(new_reader).join()
            return {'mensagem': 'Usuário cadastrado com sucesso!'}
