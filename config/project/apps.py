from django.contrib.admin.apps import AdminConfig


class NoFLIXConfig(AdminConfig):
    default_site = "config.project.admin.NoFLIXAdminSite"
