from fastapi import FastAPI

app = FastAPI()

from routes.auth_routes import auth_router
from routes.library_routes import library_router

app.include_router(auth_router)
app.include_router(library_router)


# para rodar o nosso código, executar no terminal: uvicorn main:app --reload