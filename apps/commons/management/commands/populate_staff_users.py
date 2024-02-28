import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Populates the database with staff users and assigns them to groups.'

    def handle(self, *args, **options):
        # List of staff users to create
        # Each tuple in the format: (email, password, group_name)
        staff_users = [
            [
                os.environ.get(f"STAFF_USER_{i}_EMAIL"),
                os.environ.get(f"STAFF_USER_{i}_PASSWORD"),
                'Managers'
            ]

            for i in range(1, 10)
            if os.environ.get(f"STAFF_USER_{i}_EMAIL", False)
        ]

        staff_users.append(
            [
                os.environ.get("SUPER_USER_EMAIL"),
                os.environ.get("SUPER_USER_PASSWORD"),
                'SuperAdmin'
            ]
        )

        for email, password, group_name in staff_users:
            self.create_and_assign_user(email, password, group_name)

    def create_and_assign_user(self, email, password, group_name):
        """Create a staff user and assign them to a specific group."""
        # Create user if they don't already exist
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(
                email=email,
                password=password,
                is_staff=True
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created staff user: {email}\n'
                )
            )
        else:
            user = User.objects.get(email=email)
            self.stdout.write(
                self.style.WARNING(
                    f'Staff user already exists: {email}\n'
                )
            )

        # Assign the user to the specified group
        self.assign_user_to_group(user, group_name)

    def assign_user_to_group(self, user, group_name):
        """Assigns a user to a group"""
        try:
            if group_name == "SuperAdmin":
                user.is_superuser = True
                user.save()
                return
            group = Group.objects.get(name=group_name)

            if user not in group.user_set.all():
                group.user_set.add(user)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"""Successfully added {
                            user.email} to {group_name} group\n"""
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'User {user.email} is already in {group_name} group\n'
                    )
                )
        except Group.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    f"No group found with name of {group_name}\n"
                )
            )
