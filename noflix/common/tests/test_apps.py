from django.conf import settings
from django.test import TestCase

from .base import BaseTestCaseMixin


class AppsTest(BaseTestCaseMixin, TestCase):
    def test_apps_are_registered(self):
        """Ensure all configured apps are in INSTALLED_APPS.

        Verifies that each app defined in APPLICATION_CONFIGS is
        properly registered using its AppConfig path.
        """
        installed_apps = set(settings.INSTALLED_APPS)

        for app_config_path in settings.LOCAL_APPS:
            error_msg = f"'{app_config_path}' is not registered."
            expr = {app_config_path}

            self.assertTrue(expr & installed_apps, msg=error_msg)
