from celery_file.celery import app


@app.task
def check():
    print("I am checking your stuff")
