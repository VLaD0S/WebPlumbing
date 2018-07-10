from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbing.settings')

app = Celery('WebPlumbing')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'populate-reviews-5-minutes': {
        'task': 'populate_reviews',
        'schedule': 300.0,
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

