import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')

# Run migrations on application startup
try:
    call_command('migrate', verbosity=0)
except Exception as e:
    print(f"Migration error (non-fatal): {e}")

application = get_wsgi_application()

# Vercel compatibility
app = application
