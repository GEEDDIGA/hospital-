#!/bin/bash
set -e
echo "Running database migrations..."
python manage.py migrate
echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os
if not User.objects.filter(username=os.getenv('ADMIN_USERNAME', 'admin')).exists():        User.objects.create_superuser(os.getenv('ADMIN_USERNAME', 'admin'), os.getenv('ADMIN_EMAIL', 'admin@example.com'), os.getenv('ADMIN_PASSWORD', 'admin123'))
    print('Superuser admin created successfully')
else:
    print('Superuser admin already exists')
EOF
echo "Build completed successfully!"
