from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Project Details
    AUTHOR: str = config("AUTHOR")
    AUTHOR_EMAIL: str = config("AUTHOR_EMAIL")
    PROJECT_NAME: str = config("PROJECT_NAME")
    PROJECT_DESCRIPTION: str = config("PROJECT_DESCRIPTION")

    # API V1 url prefix
    API_V1_STR: str = "/api/v1"

    # Websocket url prefix
    WS_V1_STR: str = "/ws/v1"

    # For JWT Authentication
    ALGORITHM: str = config("ALGORITHM")
    SECRET_KEY: str = config("SECRET_KEY")

    #Auth cookie name
    AUTH_COOKIE_NAME: str = "Authorization"

    #Auth cookie domain
    AUTH_COOKIE_DOMAIN: str = config("DOMAIN")

    # Token lifetime: 60 seconds * 60 minutes * 3 hours
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 3

    # Database url
    SQLALCHEMY_DATABASE_URL: str = config('DATABASE_URL')
    SQLALCHEMY_TEST_DATABASE_URL: str = config('TEST_DATABASE_URL')

    class Config:
        case_sensitive = True


settings = Settings()
