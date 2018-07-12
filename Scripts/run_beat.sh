#!/usr/bin/env bash

sleep 3
echo "deleting celerybeat.pid"
su -m myuser -c "rm celerybeat.pid"
su -m myuser -c "celery -A WebPlumbing beat"
echo "beat started"



