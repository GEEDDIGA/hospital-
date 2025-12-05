#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(username='mustafa').exists():
    User.objects.create_superuser('mustafa', 'mustafa@hospital.local', 'mustafa123@')
    print("Admin user 'mustafa' created successfully!")
else:
    print("Admin user 'mustafa' already exists.")
