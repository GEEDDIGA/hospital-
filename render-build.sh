#!/bin/bash
set -e
rm -f db.sqlite3
echo "Running database migrations..."
python manage.py migrate
echo "Creating/updating superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', 'admin123')

# Delete existing user to ensure clean slate
User.objects.filter(username=username).delete()

# Create fresh superuser
User.objects.create_superuser(username, email, password)
print(f'Superuser {username} created successfully with fresh password')
EOF

echo "Collecting static files..."
python manage.py collectstatic --noinput
