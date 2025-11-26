from fastapi import APIRouter

copy_router = APIRouter(prefix='/copy', tags=['copy'])

@copy_router.get('/')
async def get_all():
    '''
    Retorna todos os livros do banco de dados.
    '''
    return {'mensagem': 'Olá, mundo!'}
