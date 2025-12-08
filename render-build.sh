#!/bin/bash
set -e
rm -f db.sqlite3
echo "Running database migrations..."
python manage.py migrate
echo "Deleting old admin users..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').delete(); print('Old admin users deleted')"
echo "Creating new superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.create_superuser('admin', 'admin@example.com', 'admin123'); print(f'Superuser {u.username} created successfully')"
echo "Collecting static files..."
python manage.py collectstatic --noinput
