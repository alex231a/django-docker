#!/bin/bash

source /home/oyakovenko/venv/bin/activate

cd /home/oyakovenko/django-oscar

git pull origin master

pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
