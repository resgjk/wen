import os

from dotenv import load_dotenv

from sqlalchemy.engine import URL


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

postgres_url = URL.create(
    "postgresql+asyncpg",
    username=DB_USER,
    host=DB_HOST,
    database=DB_NAME,
    port=DB_PORT,
    password=DB_PASSWORD,
)
