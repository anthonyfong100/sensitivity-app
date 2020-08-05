# from celery_file.celery import app
# from db.crud import read_files
# from db.database import get_db

from app.db.crud import read_files
from app.db.database import get_db
from app.run_celery import celery_app


@celery_app.task
def check():
    print("I am checking your stuff")
