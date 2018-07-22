#!/usr/bin/env bash

echo "Starting.."
sleep 5
echo "..success!"

echo "Making plumbing migrations.."
python manage.py makemigrations plumbing
echo "..and applying plumbing migrations.."
python manage.py migrate plumbing
python manage.py migrate
echo "..finished."

echo "Attempting to start server.."
gunicorn WebPlumbing.wsgi \
    --bind 0.0.0.0:8000 \
    --workers 3


