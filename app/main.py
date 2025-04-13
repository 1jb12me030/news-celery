from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from .models import News

app = FastAPI()

@app.get("/news")
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()
