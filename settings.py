# config.py or settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = False
    ENV: str = "production"
    ALLOWED_HOSTS: list[str] = ["*"]

    class Config:
        env_file = ".env"
