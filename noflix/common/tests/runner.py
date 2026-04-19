from django.core.management import call_command
from django.test.runner import DiscoverRunner


class TestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        config = super().setup_databases(**kwargs)

        call_command("create_admin_user")

        return config
