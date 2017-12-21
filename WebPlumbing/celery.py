from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbing.settings')
app = Celery('WebPlumbing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {

    'mybuilder_60s': {
        'task': 'populate_reviews',
        'schedule': 60.0,

    }
}


app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    print('RequestL {0!r}'.format(self.request))

