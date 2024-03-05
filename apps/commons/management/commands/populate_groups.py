from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Creates necessary groups in the database.'

    def handle(self, *args, **kwargs):
        # Define the list of groups you want to ensure exist
        groups = [
            (
                'Managers',
                [
                    "add_assessment",
                    "view_assessment",
                    "change_assessment",
                    "add_assessmentpoint",
                    "view_assessmentpoint",
                    "change_assessmentpoint",
                ]
            ),

        ]

        for group_name, permission_codenames in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                permissions = Permission.objects.filter(
                    codename__in=permission_codenames
                )
                group.permissions.add(*permissions)
                group.save()
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created "{group_name}" group'))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Group "{group_name}" already exists'))
