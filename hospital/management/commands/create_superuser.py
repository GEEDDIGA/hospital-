from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser account if it does not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username='mustafa').exists():
            User.objects.create_superuser('mustafa', 'mustafa@example.com', 'mustafa123@@')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser: mustafa'))
        else:
            self.stdout.write(self.style.WARNING('Superuser mustafa already exists'))
