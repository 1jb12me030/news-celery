from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import News
from app.config.settings_config import Settings_config
# Load settings
settings = Settings_config()
# Initialize FastAPI app with debug mode
app = FastAPI(debug=settings.DEBUG)

@app.get("/news")
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()
