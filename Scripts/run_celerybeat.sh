#!/usr/bin/env bash

sleep 10

echo "STARTING BEAT!"
python manage.py makemigrations
python manage.py migrate

su -m myuser -c "celery -A WebPlumbing beat"

echo "BEAT ONLINE"


