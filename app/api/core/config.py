from typing import List

from pydantic import AnyHttpUrl
import secrets
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator
import os


class Settings(BaseSettings):
    """
    Application settings
    """

    SECRET_KEY: str = secrets.token_urlsafe(32)
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    MONGODB_URL: str
    MONGODB_DATABASE: str
    COLLECTION_NAME_GAME_SCHEMA: str
    COLLECTION_NAME_GAMES_INSTANCES: str
    COLLECTION_NAME_GAMES_FINISHED: str

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """
        Assemble CORS origins
        """
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    CLIENT_ID: str
    SERVER_URL: str
    SERVER_METADATA_URL: str

    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_URL_REALM: str

    PROTOCOL: str
    SERVER_NAME: str
    BASE_PATH: str

    PRODUCTION_MODE: bool = "https" in os.getenv("PROTOCOL")
    PROJECT_NAME: str = "Gamification v2 API"


settings = Settings()
