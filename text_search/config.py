import os

from pydantic_settings import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    # App config
    APP_NAME: str = "API Text Search Engine"
    APP_ENV: str = "develop"

    # Logging setting
    DATE_FMT: str = "%Y-%m-%d %H:%M:%S"
    LOG_DIR: str = f"{basedir}/logs/api.log"

    # Search configuration
    DATA_PATH: str = "./data/data.csv"
    INDEX_NAME: str = "text_search_index"
    TOP_K: int = 3

    ELASTICSEARCH_HOST: str = os.getenv(
        key="ELASTICSEARCH_HOST", default="http://localhost:9200"
    )


settings = Settings()
