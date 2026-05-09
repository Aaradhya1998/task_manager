
import os

from dotenv import load_dotenv


# PostgreSQL integration: load DATABASE_URL and SECRET_KEY from the local .env file.
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:your_password@localhost:5432/task_manager'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
