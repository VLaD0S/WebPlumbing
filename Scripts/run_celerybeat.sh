#!/usr/bin/env bash

sleep 10

echo "STARTING BEAT!"

su -m myuser -c "celery -A WebPlumbing beat"

echo "BEAT ONLINE"


