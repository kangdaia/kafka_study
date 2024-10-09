from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    open_oasis_key: str
    alpha_vantage_key: str
    bootstrap_servers: str = 'localhost:19094,localhost:29094,localhost:39094'

    model_config = SettingsConfigDict(
        env_file=(".env"),
        env_file_encoding="utf-8",
        json_schema_extra={
            "env": {
                "open_oasis_key":"OPEN_OASIS_KEY",
                "alpha_vantage_key": "ALPHA_VANTAGE_KEY"
            }
        }
    )

settings = Settings()