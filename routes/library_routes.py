from fastapi import APIRouter, Depends, HTTPException
from infrastructure.dependencies import get_session
from sqlalchemy.orm import Session
from models import Reader, Copy
from services import ReaderService, CopyService
from schemas import ReaderSchema, CopySchema
from exceptions.reader_exception import ReaderAlreadyExistsError
from exceptions.copy_exception import IsbnNotFoundError

library_router = APIRouter(prefix='/library', tags=['library'])

@library_router.post('/reader')
async def create_reader(reader_schema: ReaderSchema, session: Session = Depends(get_session)):
    try:
        # cria um novo leitor no banco de dados
        reader = Reader(reader_schema.id_library, reader_schema.name, reader_schema.email, reader_schema.password, reader_schema.cep)
        ReaderService.create(session, reader)

    except ReaderAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception:
        raise HTTPException(status_code=500)

@library_router.get('/reader')
async def get_all_readers(id_library: int, session: Session = Depends(get_session)):
    try:
        all_readers = ReaderService.get_all(session, id_library)
        return all_readers
    
    except Exception:
        raise HTTPException(status_code=500)

@library_router.post('/copy')
async def create_copy(copy_schema: CopySchema, session: Session = Depends(get_session)):
    try:
        CopyService.create(session, copy_schema.id_library, copy_schema.isbn, copy_schema.quantity, copy_schema.is_global)

    except IsbnNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception:
        raise HTTPException(status_code=500)

@library_router.get('/copy')
async def get_all_copies(id_library: int, session: Session = Depends(get_session)):
    try:
        all_copies = CopyService.get_all(session, id_library)
        return all_copies
    
    except Exception:
        raise HTTPException(status_code=500)
