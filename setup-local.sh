#!/bin/bash

# Hospital Management System - Local Setup Script
# This script automates the setup of the Django application locally

set -e

echo "================================================"
echo "Hospital Management System - Local Setup"
echo "================================================"
echo ""

# Check Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Create virtual environment
echo "Step 1: Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Step 2: Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "Step 3: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Create .env file
echo ""
echo "Step 4: Creating .env file..."
if [ ! -f ".env" ]; then
    cat > .env << 'EOF'
DEBUG=True
SECRET_KEY=django-insecure-local-development
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@hospital.com
ADMIN_PASSWORD=admin123
EOF
    echo "✓ .env file created"
else
    echo "✓ .env file already exists"
fi

# Run migrations
echo ""
echo "Step 5: Running database migrations..."
python manage.py migrate
echo "✓ Migrations completed"

# Create superuser
echo ""
echo "Step 6: Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@hospital.com', 'admin123')
    print('✓ Superuser created: admin')
else:
    print('✓ Superuser already exists')
EOF

# Final message
echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/admin/"
echo "Login: admin / admin123"
echo ""
echo "================================================"
