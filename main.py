from fastapi import FastAPI
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

# carrgenado as variáveis de ambiente
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

# criando a aplicação
app = FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# criando a estrutura de JWT BEARER
oauth2_schema =  OAuth2PasswordBearer(tokenUrl='auth/login-form')  

# importando os roteadores
from routers import auth_router, libraries_router, books_router, readers_router

# incluindo as rotas
app.include_router(auth_router)
app.include_router(libraries_router)
app.include_router(books_router)
app.include_router(readers_router)

# para rodar o nosso código, executar no terminal: uvicorn main:app --reload
