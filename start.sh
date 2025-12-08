#!/bin/bash
set -o errexit
# Run migrations
python manage.py migrate
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
# Collect static files
python manage.py collectstatic --no-input
# Start Gunicorn
exec gunicorn hospital.wsgi --bind 0.0.0.0:${PORT:-8000} --log-file -
