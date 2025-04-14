# config.py or settings.py
from pydantic_settings import BaseSettings
class Settings_config(BaseSettings):
    DEBUG: bool = False
    ENV: str = "production"
    ALLOWED_HOSTS: list[str] = ["*"]

    class Config:
        env_file = ".env"
