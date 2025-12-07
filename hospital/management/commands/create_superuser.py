import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create or update a superuser account using environment variables'

    def handle(self, *args, **options):
        username = os.getenv('SUPERUSER_USERNAME', 'admin')
        email = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('SUPERUSER_PASSWORD', 'admin123')

        # Delete existing user if exists
        User.objects.filter(username=username).delete()

        # Create new superuser
        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
