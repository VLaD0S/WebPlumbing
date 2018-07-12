#!/usr/bin/env bash

echo "Starting.."
sleep 20
echo "..success!"

echo "Making plumbing migrations.."
python manage.py makemigrations plumbing
echo "..and applying plumbing migrations.."
python manage.py migrate plumbing
echo "..finished."

echo "Attempting to start server.."
python manage.py runserver 0.0.0.0:8000


