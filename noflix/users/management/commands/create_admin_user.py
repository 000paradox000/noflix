from typing import Any

from django.core.management.base import BaseCommand

from noflix.common import utilities


class Command(BaseCommand):
    """Create the default admin superuser."""

    help = "Create admin/admin superuser"

    def handle(self, *args: Any, **options: Any) -> None:
        """Execute the management command.

        Args:
            *args: Positional command arguments.
            **options: Parsed command options.
        """
        username = "admin"
        password = "admin"  # nosec B105
        email = "admin@project.local"
        first_name = "Admin"
        last_name = "User"

        if utilities.user_exists(username=username):
            message = "User 'admin' already exists."
            self.stdout.write(self.style.WARNING(message))
            return

        utilities.create_admin_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        message = "User 'admin' was created successfully."
        self.stdout.write(self.style.SUCCESS(message))
