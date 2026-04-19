from pathlib import Path

from .base import *

# -----------------------------------------------------------------------------
# Environment

ENVIRONMENT_NAME = Path(__file__).resolve().stem

DEBUG = True
ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = f"config.wsgi.{ENVIRONMENT_NAME}.application"

SITE_TITLE = f"[{ENVIRONMENT_NAME}] {SITE_TITLE}"
SITE_HEADER = f"[{ENVIRONMENT_NAME}] {SITE_HEADER}"

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": PROJECT_DIR / "db" / "noflix.db",
    },
}

# -----------------------------------------------------------------------------
# Email

# Store outgoing emails as files during local development.
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = EMAIL_DIR
