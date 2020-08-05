from celery import Celery

app = Celery("file checker", include=["celery_file.tasks"])

app.config_from_object("celery_file.celeryconfig")

app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "celery_file.tasks.check",
        "schedule": 10.0,
    }
}
