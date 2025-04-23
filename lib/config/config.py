import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL", "sqlite:///./test.db")

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", "DEV")
