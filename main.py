from fastapi import FastAPI

app = FastAPI()

from routes.copy_routes import copy_router

app.include_router(copy_router)

# para rodar o nosso código, executar no terminal: uvicorn main:app --reload