from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbing.settings')
app = Celery('WebPlumbing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


    
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'sum_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },

    'add-every-5-seconds': {
        'task': 'populate_reviews',
        'schedule':120.0
    }
}

app.conf.timezone = 'UTC'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

@app.task
def test(arg):
    print(arg)  

@app.task(bind=True)
def debug_task(self):
    print('RequestL {0!r}'.format(self.request))

