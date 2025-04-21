import os

class Config:
    DEBUG = os.getenv('DEBUG', True)
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./catalog.db')

config = Config()
