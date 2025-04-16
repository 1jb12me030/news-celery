import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

DATABASE_URL = os.getenv("DATABASE_URL")
# Database URL
#DATABASE_URL = #"postgresql://postgres:1234@localhost:5432/news_db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#deploy project on ec2
# Base for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🚀 Add this line to ensure Alembic detects models
from app.models import News  # Import all models here
