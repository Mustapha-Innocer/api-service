import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://username:password@host:port/dbname")

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", "DEV")
