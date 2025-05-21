#!/bin/bash

HOST="mysql"
PORT=3306

echo "Waiting for $HOST:$PORT to be available..."

while ! nc -z "$HOST" "$PORT"; do
  sleep 1
done

echo "$HOST:$PORT is now available!"

# sleep 10
echo "Done Waiting !!"
python innerview/manage.py makemigrations
python innerview/manage.py migrate
python innerview/manage.py create_superuser
python innerview/manage.py runserver 0.0.0.0:80
