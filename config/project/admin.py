from django.conf import settings
from django.contrib import admin


class NoFLIXAdminSite(admin.AdminSite):
    site_header = settings.SITE_HEADER
    site_title = settings.SITE_TITLE
    index_title = ""
