import environ

from .original import *

# -----------------------------------------------------------------------------
# Paths

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "noflix"

# -----------------------------------------------------------------------------
# Environment variables

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / ".env")

# -----------------------------------------------------------------------------
# Secret key

SECRET_KEY = env("DJANGO_SECRET_KEY")

# -----------------------------------------------------------------------------
# Default Data Types

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------------
# Application definition

DJANGO_APPS = INSTALLED_APPS
DJANGO_APPS[0] = "config.project.apps.NoFLIXConfig"

THIRD_PARTY_APPS = [
    "django_extensions",
]

LOCAL_APPS = [
    "noflix.common.apps.CommonConfig",
    "noflix.users.apps.UsersConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# -----------------------------------------------------------------------------
# Templates

TEMPLATES[0]["DIRS"] = [
    PROJECT_DIR / "templates",
]

# -----------------------------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_TZ = True

# -----------------------------------------------------------------------------
# Static

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]
STATIC_ROOT = PROJECT_DIR / "static_root"

# -----------------------------------------------------------------------------
# Media

MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR / "media"

# -----------------------------------------------------------------------------
# Dirs

TEMPORAL_DIR = PROJECT_DIR / "temporal"

FILES_DIR = PROJECT_DIR / "files"
INPUT_FILES_DIR = FILES_DIR / "input"
OUTPUT_FILES_DIR = PROJECT_DIR / "output"

EMAIL_DIR = TEMPORAL_DIR / "email"

# -----------------------------------------------------------------------------
# Site title

SITE_TITLE = "NoFLIX"
SITE_HEADER = "NoFLIX"

# -----------------------------------------------------------------------------
# Test

TEST_RUNNER = "noflix.common.tests.runner.TestRunner"
