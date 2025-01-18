from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    OPENAI_API_KEY: str

    UVICORN_HOST: str
    UVICORN_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
    )


settings = Settings()
