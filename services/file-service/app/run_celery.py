import os

from celery import Celery

celery_app = Celery("file checker", include=["app.celery_file.tasks"])

celery_app.config_from_object("app.celery_file.celeryconfig")

celery_app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "app.celery_file.tasks.check",
        "schedule": 10.0,
    },
}
