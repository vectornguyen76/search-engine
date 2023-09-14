import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    # App config
    APP_NAME: str = "API Image Search Engine"
    APP_ENV: str = "develop"
    
    # Logging setting
    DATE_FMT: str = '%Y-%m-%d %H:%M:%S'
    LOG_DIR: str = f'{basedir}/logs/api.log'
    
    IMAGEDIR:str = "assets/uploaded_images/"
    
    # Search configuration
    FEATURES_PATH:str = "./data/array_features.npz"
    DATA_PATH:str = "./data/data.csv" 
    DIMENSIONS:int = 1000
    TOP_K:int = 3
    
    # Faiss configuration
    INDEX_PATH:str = "./faiss_store/index.faiss"
    
    # Qdrant configuration
    QDRANT_GRPC_URL:str = os.environ.get("QDRANT_GRPC_URL", "http://localhost:6334")
    QDRANT_COLLECTION:str = "image-search-engine"

settings = Settings()