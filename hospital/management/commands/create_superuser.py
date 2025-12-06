from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create or update a superuser account'

    def handle(self, *args, **options):
        username = 'mustafa'
        email = 'mustafa@example.com'
        password = 'mustafa123@@'
        
        # Delete existing user if exists
        User.objects.filter(username=username).delete()
        
        # Create new superuser
        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
