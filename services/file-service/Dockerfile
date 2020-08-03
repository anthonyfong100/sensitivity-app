FROM python:3.7-slim

COPY Pipfile* /
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r /requirements.txt

COPY . ./file-service
WORKDIR /file-service
EXPOSE 7000

RUN mkdir ./data
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]