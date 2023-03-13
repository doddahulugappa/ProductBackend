from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_api.settings')

app = Celery('product_api')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Dubai')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

