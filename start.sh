#!/bin/bash
set -o errexit

# Run migrations
python manage.py migrate

# Create or reset superuser
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', 'admin123')

# Delete existing user with same username to ensure clean slate
User.objects.filter(username=username).delete()

# Create superuser
User.objects.create_superuser(username, email, password)
print(f'Superuser {username} created successfully with fresh password')
EOF

# Collect static files
python manage.py collectstatic --no-input

# Start Gunicorn
exec gunicorn hospital.wsgi --bind 0.0.0.0:${PORT:-8000} --log-file -
