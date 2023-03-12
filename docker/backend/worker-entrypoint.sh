#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run celery worker & beat
#celery -A backend worker --loglevel=info --concurrency 1 -E

#celery -A backend beat --loglevel=info --scheduler=django_celery_beat.schedulers.DatabaseScheduler

