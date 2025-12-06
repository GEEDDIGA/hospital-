from django.apps import AppConfig
from django.core.management import call_command
from django.db.utils import OperationalError
import sys


class HospitalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital'
    verbose_name = 'Hospital Management System'

    def ready(self):
        """Run migrations when Django starts"""
        # Only run migrations if we're in server mode (gunicorn/wsgi), not during tests
        if 'test' not in sys.argv and 'manage.py' not in sys.argv[0]:
            try:
                # Run migrations
                call_command('migrate', verbosity=0)
            except (OperationalError, Exception) as e:
                # If DB isn't ready yet, that's fine - will retry on next request
                pass
