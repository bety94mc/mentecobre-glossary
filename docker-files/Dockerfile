# pull official base image
FROM python:3.11 AS builder

# set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=main.settings.local \
    LC_ALL=es_ES.UTF-8

# update apt and install dependencies
RUN apt-get update && apt-get install -y locales locales-all gcc musl-dev python3-dev libffi-dev libssl-dev \
    && pip install --upgrade pip

# install python dependencies
COPY requirements.txt /app/src/requirements.txt
RUN pip install --no-cache-dir -r /app/src/requirements.txt


COPY . /app

WORKDIR /app/src

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
