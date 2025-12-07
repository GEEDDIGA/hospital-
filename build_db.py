import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')
django.setup()

# Create superuser
if not User.objects.filter(username='mustafa').exists():
    User.objects.create_superuser('mustafa', 'mustafa@example.com', 'mustafa123@')
    print('Superuser created successfully')
else:
    print('Superuser already exists')

# Create admin superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'geeddiga@gmail.com', 'Hospital@Admin123')
    print('Admin superuser created successfully')
else:
    print('Admin superuser already exists')
