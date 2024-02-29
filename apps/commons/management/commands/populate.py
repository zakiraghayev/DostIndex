from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Runs all populate commands to set up the database.'

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS(
                'Starting database population...\n'
            )
        )

        # Call populate_groups command
        self.stdout.write(self.style.SUCCESS('Populating groups...\n'))
        call_command('populate_groups')

        # Call populate_staff_users command
        self.stdout.write(self.style.SUCCESS('Populating staff users...\n'))
        call_command('populate_staff_users')

        # Call populate_staff_users command
        self.stdout.write(self.style.SUCCESS('Populating articles & sections'))
        call_command('populate_articles_and_sections')

        self.stdout.write(
            self.style.SUCCESS(
                'Database population complete.\n'
            )
        )
