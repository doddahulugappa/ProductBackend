#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 4
done


python manage.py collectstatic --noinput

# createsuperuser
python manage.py createsuperuser --noinput

gunicorn backend.wsgi --bind 0.0.0.0:80 --workers 4 --threads 4
