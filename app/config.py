import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(dotenv_path=find_dotenv())


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    X_API_KEY_TOKEN = os.getenv("X_API_KEY_TOKEN")


settings = Settings()
