from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator


class Settings(BaseSettings):
    open_oasis_key: str

    model_config = SettingsConfigDict(
        env_file=(".env"),
        env_file_encoding="utf-8",
        json_schema_extra={
            "env": {
                "open_oasis_key":"OPEN_OASIS_KEY"
            }
        }
    )

settings = Settings()