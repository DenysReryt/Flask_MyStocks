"""
Module to handle application configuration settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    """
        Class to define application settings.
    """

    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_USER: str = os.getenv('DB_USER')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_HOST: str = os.getenv('DB_HOST')

    def __init__(self):
        pass


settings = Settings()