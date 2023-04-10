from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_host: str = "postgresql+asyncpg://localhost@r5-db:5432/r5"


@lru_cache()
def get_settings():
    return Settings()