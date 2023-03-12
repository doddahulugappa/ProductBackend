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

# Celery Beat Settings
app.conf.beat_schedule = {'test_run': {
    'task':'products.tasks.send_activation_mail',
    'schedule': crontab(minute=0, hour=8)  # every day at 8am in morning
}
}

