# Mentecobre-glossary

## Introduction
This project build a django web app designed to show a glossary of terms in both 
English and Spanish. The terms have a link to the Coppermind page where the term is
explained. The terms are stored in a SQL database and can be managed through the Django
admin panel.

## Build
The repository has the necessary files to build this project in Docker:
- Dockerfile
- requirements.txt 
- docker-compose.yml

To do this, execute the following commands in order:

```
docker-compose -f docker-files/docker-compose.yml up --build
```

This will build the images in docker and run a container with a PostgresSQL database
and a Django web app.

First, we should open a terminal inside the django container and the run the following
commands in order:

```
python manage.py migrate
```

For security purposes, no SECRET_KEY should be included in the code. So, a .env file is needed to be created 
and secret_key included there such as:
```
DJANGO_SECRET_KEY = 'askdjlk123hbasdbhjasd1@#aso123€¬'
```
The key is literally anything, it has no relevance to the development environment.

## APPS

The project uses Django with PostgreSQL. It also uses html and css to build the template part.
This project has one app: mentecobre

### mentecobre
This app is the main part of the project. It has 1 model:
 - Glossary. Model to have a list of terms in both languages

The different views and templates that user can interact with will be located in this app.
The django-admin is a key part of this app, as it's the main tool to manage the database.
