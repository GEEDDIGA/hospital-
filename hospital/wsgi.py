import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')

application = get_wsgi_application()

# Auto-run migrations on startup
try:
    from django.core.management import call_command
    call_command('run_migrations')
except Exception as e:
    import sys
    print(f'Migration error: {e}', file=sys.stderr)

# Vercel compatibility
app = application
