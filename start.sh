#!/bin/bash
set -o errexit

# Run migrations
python manage.py migrate

python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
EOF

# Collect static files
python manage.py collectstatic --no-input

# Start Gunicorn
exec gunicorn hospital.wsgi --bind 0.0.0.0:${PORT:-8000} --log-file -
