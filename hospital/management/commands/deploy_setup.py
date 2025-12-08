from django.core.management.base import BaseCommand
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = 'Deploy setup: run migrations, collect static files, and create/update superuser'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Running database migrations...'))
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Collecting static files...'))
        call_command('collectstatic', '--no-input')

        self.stdout.write(self.style.SUCCESS('Creating/updating superuser...'))
        from django.contrib.auth.models import User

        username = os.getenv('ADMIN_USERNAME', 'admin')
        email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
        password = os.getenv('ADMIN_PASSWORD', 'admin123')

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.email = email
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} updated successfully'))
        else:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))

        self.stdout.write(self.style.SUCCESS('Deploy setup completed successfully!'))
