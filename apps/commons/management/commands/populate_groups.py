from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Creates necessary groups in the database.'

    def handle(self, *args, **kwargs):
        # Define the list of groups you want to ensure exist
        groups = ['Managers']

        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created "{group_name}" group'))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Group "{group_name}" already exists'))
