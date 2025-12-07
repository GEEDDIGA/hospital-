#!/bin/bash
set -o errexit

# Run migrations
python manage.py migrate
echo "Migrations completed"
if [ $? -ne 0 ]; then exit 1; fi

# Collect static files
python manage.py collectstatic --no-input


# Create superuser
python manage.py create_superuser
