import os

from celery import Celery

celery_app = Celery("file checker", include=["app.celery_file.tasks"])

celery_app.config_from_object("app.celery_file.celeryconfig")

celery_app.conf.beat_schedule = {
    "update_sensitivity_score": {
        "task": "app.celery_file.tasks.update_sensitivity_score",
        "schedule": 10.0,
    },
}
