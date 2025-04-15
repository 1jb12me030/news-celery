# config.py or settings.py
from pydantic_settings import BaseSettings
from pydantic import BaseModel

class Settings_config(BaseSettings):
    # General application settings
    DEBUG: bool = False
    ENV: str = "production"
    ALLOWED_HOSTS: list[str] = ["*"]

    # Database and Docker settings
    database_url: str
    docker_username: str
    docker_password: str
    ec2_host: str
    ec2_user: str
    ec2_ssh_key: str

    class Config:
        env_file = ".env"  # Load environment variables from .env file
        extra = "allow"     # Allow extra fields if necessary

# Example of how to instantiate the settings
settings = Settings_config()