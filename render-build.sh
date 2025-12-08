#!/bin/bash
set -e
rm -f db.sqlite3
echo "Running database migrations..."
python manage.py migrate
echo "Creating/updating superuser..."
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get(username='admin'); u.set_password('admin123'); u.save(); print(f'Superuser {u.username} password updated')"
echo "Collecting static files..."
python manage.py collectstatic --noinput
