from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from lib.mytask1 import MyTask1
from lib.mytask2 import MyTask2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo2.settings')
app = Celery('celery_demo2')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

mytask1 = app.register_task(MyTask1())
mytask2 = app.register_task(MyTask2())
