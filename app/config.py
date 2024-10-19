import os

class Settings:
    FLYHUB_API_KEY: str = os.getenv("FLYHUB_API_KEY")
    FLYHUB_USERNAME: str = os.getenv("FLYHUB_USERNAME")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()