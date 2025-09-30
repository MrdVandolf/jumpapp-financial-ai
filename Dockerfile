FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /jump

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app
CMD ["mkdir", "/jump/logs"]

EXPOSE 8080

COPY ./startup.py ./startup.py
COPY ./.env ./.env
COPY ./certificate.pem ./certificate.pem
COPY ./key.pem ./key.pem
CMD ["python", "-m", "startup", "--env", ".env", "--log-level", "debug", "--execute-migrations"]