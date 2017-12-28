#!/usr/bin/env bash


sleep 10

echo "SLEPT WELL!"
su -m myuser -c "celery -A WebPlumbing worker"  
echo "WORKER ONLINE!"


