#!/bin/bash
set -e
echo "Running database migrations..."
python manage.py migrate
echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser admin created successfully')
else:
    print('Superuser admin already exists')
EOF
echo "Build completed successfully!"
