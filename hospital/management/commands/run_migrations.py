from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run makemigrations and migrate to ensure database is up to date'

    def handle(self, *args, **options):
        self.stdout.write('Starting migrations...')
        try:
            call_command('makemigrations')
            self.stdout.write(self.style.SUCCESS('makemigrations completed successfully'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'makemigrations error (non-critical): {e}'))
        
        try:
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('migrate completed successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'migrate error: {e}'))
            raise
