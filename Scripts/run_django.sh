#!/usr/bin/env bash

echo "Starting.."
sleep 3
echo "..success!"

echo "Making migrations.."
python manage.py makemigrations
echo "..and applying migrations.."
python manage.py migrate
echo "..finished."

echo "Attempting to start server.."
python manage.py runserver 0.0.0.0:8000



