#!/bin/bash
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Deleting old admin users..."
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').delete()"

echo "Creating new superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.getenv('SUPERUSER_USERNAME', 'admin')
email = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('SUPERUSER_PASSWORD', 'admin123')

try:
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created successfully')
except Exception as e:
    print(f'Error: {e}')
EOF

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear
