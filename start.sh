#!/bin/bash
set -o errexit

echo "Starting Django application setup..."

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser with error handling
echo "Setting up superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.getenv('SUPERUSER_USERNAME', 'admin')
email = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('SUPERUSER_PASSWORD', 'admin123')

try:
    # Delete existing user with same username
    User.objects.filter(username=username).delete()
    
    # Create new superuser
    user = User.objects.create_superuser(username, email, password)
    print(f'✓ Superuser "{username}" created successfully')
    print(f'  Username: {username}')
    print(f'  Password: {password}')
    print(f'  Email: {email}')
except Exception as e:
    print(f'✗ Error creating superuser: {str(e)}')
    exit(1)
EOF

echo "Migrations and superuser setup completed successfully"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

# Start Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn hospital.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers ${GUNICORN_WORKERS:-2} --timeout 120 --access-logfile - --error-logfile -
