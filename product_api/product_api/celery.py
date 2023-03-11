from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_api.settings')

app = Celery('product_api')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Dubai')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

# Celery Beat Settings
app.conf.beat_schedule = {'test_run': {
    'task':'products.tasks.send_activation_mail',
    'schedule': crontab()
    # 'schedule': crontab(minute=0, hour=0)  # every day at mid night
}
}

