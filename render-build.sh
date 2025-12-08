#!/bin/bash
set -e
echo "Running database migrations..."
python manage.py migrate
echo "Creating/updating superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', 'admin123')

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.email = email
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f'Superuser {username} updated successfully')
else:
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created successfully')
EOF
echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Build completed successfully!"
