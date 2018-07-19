#!/usr/bin/env bash

sleep 3
echo "deleting celerybeat.pid"
rm celerybeat.pid
celery -A WebPlumbing beat
echo "beat started"



