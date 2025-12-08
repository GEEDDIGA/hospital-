#!/bin/bash

set -o errexit

echo "Starting Django application setup..."

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create or reset superuser
echo "Setting up superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

# Delete existing user with same username
User.objects.filter(username=username).delete()

# Create new superuser
User.objects.create_superuser(username, email, password)
print(f'Superuser {username} created successfully with fresh password')
EOF

echo "Migrations and superuser setup completed successfully"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Start Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn hospital.wsgi --bind 0.0.0.0:${PORT:-8000} --log-file -
