from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    weather_api_key: str
    bootstrap_servers: str = 'localhost:19094,localhost:29094,localhost:39094'

    model_config = SettingsConfigDict(
        env_file=(".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()