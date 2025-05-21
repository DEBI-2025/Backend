FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && pip install --upgrade pip && pip install pipenv && apt-get install  build-essential pkg-config libmariadb-dev  -y

COPY  Pipfile Pipfile.lock ./

RUN pipenv  requirements >>  requirements.txt && pip install -r requirements.txt

COPY . .

# ARG super_user_email
# # ENV super_user_email=$super_user_email

# ARG super_user_pass
# ENV super_user_pass=$super_user_pass
RUN chmod +x /app/start.sh
#RUN python innerview/manage.py makemigrations && python innerview/manage.py migrate
# RUN python innerview/manage.py create_superuser

EXPOSE 80
CMD ["/app/start.sh"]

