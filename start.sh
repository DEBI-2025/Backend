#!/bin/bash
sleep 10
echo "Done Waiting !!"
python innerview/manage.py makemigrations
python innerview/manage.py migrate
python innerview/manage.py create_superuser
python innerview/manage.py runserver 0.0.0.0:80
