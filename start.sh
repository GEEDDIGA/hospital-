#!/bin/bash
set -o errexit

# Run migrations
python manage.py migrate
python manage.py create_superuser

# Collect static files  
python manage.py collectstatic --no-input

# Start Gunicorn
exec gunicorn hospital.wsgi --log-file -
