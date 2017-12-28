#!/usr/bin/env bash

sleep 10

echo "SLEPT WELL!"
python manage.py makemigrations
python manage.py migrate
su -m myuser -c "celery -A WebPlumbing worker"  
echo "WORKER ONLINE!"


