#!/bin/bash
set -o errexit

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input


# Create superuser
python manage.py create_superuser
