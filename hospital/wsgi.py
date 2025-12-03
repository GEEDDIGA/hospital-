import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')

application = get_wsgi_application()

# Initialize database migrations and create superuser on startup
import django
from django.core.management import call_command
from django.contrib.auth.models import User

django.setup()

try:
    # Run migrations
    call_command('migrate', verbosity=0)
    
    # Create superuser if doesn't exist
    if not User.objects.filter(username='mustafa').exists():
        User.objects.create_superuser(
            username='mustafa',
            email='mustafa123@',
            password='mustafa123@'
        )
except Exception as e:
    print(f'Initialization error: {e}')
