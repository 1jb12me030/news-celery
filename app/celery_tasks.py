from celery import Celery
from sqlalchemy.orm import Session
from .database import SessionLocal
from .services import fetch_news, save_news  # Import updated functions
from celery.schedules import crontab

# Initialize Celery
celery_app = Celery("news_tasks", broker="redis://localhost:6379/0")

# Celery Configuration
celery_app.conf.update(
    broker_url="redis://localhost:6379/0",
    result_backend="redis://localhost:6379/0",
    broker_connection_retry_on_startup=True,
    accept_content=["json"],
    task_serializer="json",
)

# Celery Task to fetch and store news
@celery_app.task
def fetch_and_store_news():
    """Fetch news from API and store it in the database."""
    #print("Fetching and storing news...")  # Debugging log
    db: Session = SessionLocal()
    news_data = fetch_news()
    
    if "articles" in news_data:
        for article in news_data["articles"]:
            save_news(db, {
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt"),
            })
    
    db.close()
    #print("News fetching completed.")  # Debugging log


# Celery Beat Schedule (runs fetch_and_store_news every minute)
celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "app.celery_tasks.fetch_and_store_news",
        "schedule": crontab(minute="*"),  # Runs every minute
    }
}
celery_app.conf.timezone = "UTC"
