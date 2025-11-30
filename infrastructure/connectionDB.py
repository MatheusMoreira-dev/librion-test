from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# url do banco de dado
url_database = 'sqlite:///database.db'

# conexão com o banco de dados
db = create_engine(url_database)

# cria a sessão do banco de dados
SessionLocal = sessionmaker(bind=db)

# base do banco de dados
Base = declarative_base()

# para criar uma migration no banco de dados, use: alembic revision --autogenerate -m "mensagem"

# para executar a migration, use: alembic upgrade head
