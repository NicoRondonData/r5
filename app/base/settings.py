from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://localhost@r5-db:5432/r5"
    oreilly_api_url = "https://learning.oreilly.com/api/v2/"


@lru_cache()
def get_settings():
    return Settings()
