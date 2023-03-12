#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run celery worker & beat
#celery -A backend worker --loglevel=info --concurrency 1 -E
nohup docker exec -it api_container celery -A product_api worker --loglevel=info --concurrency 1 -E > /dev/null &

#celery -A backend beat --loglevel=info --scheduler=django_celery_beat.schedulers.DatabaseScheduler
nohup docker exec -it api_container celery -A product_api beat --loglevel=info > /dev/null &

