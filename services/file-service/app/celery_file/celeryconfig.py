import os

broker_url = os.getenv("CELERY_BROKER")
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = True
