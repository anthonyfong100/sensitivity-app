# from celery_file.celery import app
# from db.crud import read_files
# from db.database import get_db

from app.db.crud import read_files, update_file_sensitivity
from app.db.database import get_db
from app.run_celery import celery_app
from app.sensitivity import calculate_sensitivity_score
from app.utils import read_file


@celery_app.task
def update_sensitivity_score():
    db = next(get_db())
    files = read_files(db)

    for file in files:
        file_content = read_file(file.filepath)
        sensitivity_score = calculate_sensitivity_score(file_content)
        update_file_sensitivity(db, {"id": file.id}, sensitivity_score)
