# app/core/config.py

from pydantic_settings import BaseSettings
from pydantic import Extra

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str

    # Tell Pydantic v2 to read from .env and ignore any extra vars
    model_config = {
        "env_file": ".env",
        "extra": Extra.ignore,
    }

settings = Settings()
