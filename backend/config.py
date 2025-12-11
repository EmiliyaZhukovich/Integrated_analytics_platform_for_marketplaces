import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'Analytics Platform for Marketplaces'
    debug: bool = True
    database_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:4521@localhost:5432/analytics_platform")
    # cors_origins: list = [
    #     "http://localhost:5173",
    #     "http://localhost:3000",
    #     "http://127.0.0.1:5173",
    #     "http://127.0.0.1:3000",
    # ]
    # static_dir: str = "static"
    # image_dir: str = "static/images"

    class Config:
        env_file = '.env'

settings = Settings()
