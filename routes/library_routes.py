from fastapi import APIRouter, Depends, HTTPException
from infrastructure.dependencies import get_session
from sqlalchemy.orm import Session
from models import Reader
from services import ReaderService
from schemas import ReaderSchema
from exceptions.reader_exception import ReaderAlreadyExistsError

library_router = APIRouter(prefix='/library', tags=['library'])

@library_router.post('/reader')
async def create_reader(reader_schema: ReaderSchema, session: Session = Depends(get_session)):
    try:
        # cria um novo leitor no banco de dados
        reader = Reader(reader_schema.id_library, reader_schema.name, reader_schema.email, reader_schema.password, reader_schema.cep)
        ReaderService.create(session, reader)

    except ReaderAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500)
