import requests
from sqlalchemy.orm import Session
from app.models import News

NEWS_API_KEY = "7e4d4419add548a085633a31ca038f07"

def fetch_news():
    """Fetch latest news articles from News API."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    # Debugging: Print API response
    print("News API Response:", data)

    return data
def save_news(db: Session, news_data: dict):
    """Check if news article exists before inserting."""
    existing_news = db.query(News).filter(News.url == news_data["url"]).first()
    for id in news_data["articles"]:
        if id%5 == 0:
            news = News(title=news_data["articles"][id]["title"]),
            description=news_data["articles"][id]["description"],
            url=news_data["articles"][id]["url"]
            db.delete(news, description, url)
        
    if not existing_news:  # Insert only if URL is not present
        new_entry = News(
            title=news_data["title"],
            description=news_data.get("description"),
            url=news_data["url"],
            published_at=news_data.get("published_at")
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry
    return None  # News with the same URL already exists

# def save_news(db: Session, news_data: dict):
#     print("2222newsdata:", news_data)
#     """Check if news article exists before inserting."""
#     existing_news = db.query(News).filter(News.url == news_data["url"]).first()
    
#     if existing_news:
#         # Print detailed information about the existing news
#         print("Existing News Article Found:")
#         print(f"Title: {existing_news.title}")
#         print(f"Description: {existing_news.description}")
#         print(f"URL: {existing_news.url}")
#         print(f"Published At: {existing_news.published_at}")
#     else:
#         print("No existing news found. Proceeding with insertion.")
    
#     if not existing_news:  # Insert only if URL is not present
#         new_entry = News(
#             title=news_data["title"],
#             description=news_data.get("description"),
#             url=news_data["url"],
#             published_at=news_data.get("published_at")
#         )
#         db.add(new_entry)
#         db.commit()
#         db.refresh(new_entry)
#         return new_entry
    
#     return None  # News with the same URL already exists

