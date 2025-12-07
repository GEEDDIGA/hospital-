#!/bin/bash
set -e
echo "Running database migrations..."
python manage.py migrate
echo "Creating superuser..."
python manage.py init_superuser
echo "Build completed successfully!
