import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# строка подключения к базе данных PostgreSQL
database_url = database_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{5432}/{os.getenv('DB_NAME')}"

# Создание объекта Engine для подключения
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency для использования в маршрутах
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
