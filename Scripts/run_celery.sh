#!/usr/bin/env bash

sleep 3

su -m myuser -c "celery -A WebPlumbing worker -l info"  
echo "review extractor worker starterd"

