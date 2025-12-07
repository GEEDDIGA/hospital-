#!/bin/bash
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='mustafa').exists():
    User.objects.create_superuser('mustafa', 'mustafa123@example.com', 'mustafa123')
    print('Superuser "mustafa" created successfully')
else:
    print('Superuser "mustafa" already exists')
END

echo "Build completed successfully!"
python manage.py init_superuser
