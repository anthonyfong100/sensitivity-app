import os

from dotenv import load_dotenv

load_dotenv()

broker_url = os.getenv("CELERY_BROKER_URL")
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = True
