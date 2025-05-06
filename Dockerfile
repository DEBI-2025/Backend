FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && pip install --upgrade pip && pip install pipenv

COPY  Pipfile Pipfile.lock ./

RUN pipenv  requirements >>  requirements.txt && pip install -r requirements.txt

COPY . .


RUN python innerview/manage.py makemigrations && python innerview/manage.py migrate
RUN python innerview/manage.py create_superuser

EXPOSE 80
CMD [ "python","innerview/manage.py" , "runserver" , "0.0.0.0:80" ]

