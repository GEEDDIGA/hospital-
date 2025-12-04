#!/bin/bash
set -e

echo "Running Django migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='mustafa').exists():
    User.objects.create_superuser('mustafa', 'mustafa@example.com', 'mustafa123@')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
END

echo "Initialization complete"
