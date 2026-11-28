import logging
from pathlib import Path
from typing import Annotated
from urllib.parse import urlparse

from fastapi import Depends, Request
from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"

logger = logging.getLogger(__name__)

class AppSettings(BaseModel):
    name: str = "Posts API"
    debug: bool = False


class DatabaseSettings(BaseModel):
    url: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore"
    )
    database_url: str
    database_url_sync: str

    @property
    def app(self) -> AppSettings:
        return AppSettings()

    @property
    def db(self) -> DatabaseSettings:
        return DatabaseSettings(url=self.database_url)

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        logger.info(f"validating database_url: {value}")
        parsed = urlparse(value)
        if parsed.scheme not in {"postgresql", "postgresql+asyncpg"}:
            raise ValueError("database_url must be postgresql or postgresql+asyncpg")

        if not parsed.hostname:
            raise ValueError("database_url must have a hostname")

        dbname  = (parsed.path or "").lstrip("/")
        if not dbname:
            raise ValueError("database_url must have a database name")

        if parsed.port is not None and not (1 <= parsed.port <= 65535):
            raise ValueError("database_url must have a port number between 1 and 65535")

        return value


def get_settings(request: Request) -> Settings:
    return request.app.state.settings


SettingsDeps = Annotated[Settings, Depends(get_settings)]
