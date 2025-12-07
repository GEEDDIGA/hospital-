from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@hospital.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('Superuser admin already exists'))
