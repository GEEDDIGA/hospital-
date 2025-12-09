#!/bin/bash
set -o errexit

echo "Running Django migrations..."
python manage.py migrate --no-input

echo "Creating superuser..."
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME', 'admin')
email = os.environ.get('SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('SUPERUSER_PASSWORD', 'admin123')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created')
else:
    print(f'Superuser {username} already exists')
EOF

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "Starting server..."
gunicorn hospital.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2
