#!/usr/bin/env bash

sleep 10

echo "Starting app. Migrating"
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

echo "Finished migration. starting server..."
python manage.py runserver 0.0.0.0:8000

