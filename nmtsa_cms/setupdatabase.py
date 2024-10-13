import json
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Set up database: make migrations, merge conflicts, migrate, and load dummy data'

    def handle(self, *args, **options):
        self.stdout.write('Making migrations...')
        call_command('makemigrations')

        self.stdout.write('Checking for merge conflicts...')
        try:
            call_command('makemigrations', '--merge', '--noinput')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Merge conflict detected: {e}'))
            self.stdout.write('Please resolve conflicts manually and run the command again.')
            return

        self.stdout.write('Applying migrations...')
        call_command('migrate')