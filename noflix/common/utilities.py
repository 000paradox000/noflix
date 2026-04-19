import json
import secrets
import string
import uuid
from pathlib import Path
from typing import Any

from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from django.utils import timezone
from django.utils.lorem_ipsum import paragraphs


def get_visitor_ip(request: HttpRequest | None = None) -> str:
    """Return the visitor IP address.

    Args:
        request: Django HTTP request instance.

    Returns:
        The detected IP address. Returns ``"127.0.0.1"`` when unavailable.
    """
    if request is None:
        return "127.0.0.1"

    meta = request.META
    x_forwarded_for = meta.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()

    return meta.get("REMOTE_ADDR", "127.0.0.1")


def create_admin_user(
    username: str,
    password: str,
    first_name: str,
    last_name: str,
    email: str,
) -> User:
    """Create and return a Django superuser.

    Args:
        username: Username for the admin user.
        password: Password for the admin user.
        first_name: First name.
        last_name: Last name.
        email: Email address.

    Returns:
        The created user instance.
    """
    return User.objects.create_superuser(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )


def create_normal_user(
    username: str,
    password: str,
    first_name: str,
    last_name: str,
    email: str,
    is_staff: bool = False,
) -> User:
    """Create and return a regular Django user.

    Args:
        username: Username for the user.
        password: Password for the user.
        first_name: First name.
        last_name: Last name.
        email: Email address.
        is_staff: Whether the user has staff access.

    Returns:
        The created user instance.
    """
    return User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
    )


def add_user_to_group(user: User, group_name: str) -> None:
    """Add a user to a Django auth group.

    Creates the group if it does not exist.

    Args:
        user: Django user instance.
        group_name: Group name.
    """
    group, _ = Group.objects.get_or_create(name=group_name)
    user.groups.add(group)


def user_exists(username: str) -> bool:
    """Return whether a user with the given username exists.

    Args:
        username: Username to check.

    Returns:
        ``True`` if the user exists, otherwise ``False``.
    """
    return User.objects.filter(username=username).exists()


def generate_hash_value() -> str:
    """Return a unique hash string."""
    return uuid.uuid4().hex


def _json_default(value: Any) -> Any:
    """Serialize values unsupported by ``json.dumps``.

    Args:
        value: Object to serialize.

    Returns:
        A JSON-serializable representation.
    """
    if isinstance(value, (set, frozenset)):
        return list(value)

    if isinstance(value, Path):
        return str(value)

    if isinstance(value, uuid.UUID):
        return value.hex

    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")

    return str(value)


def to_json(data: Any) -> str:
    """Return a pretty JSON string.

    Args:
        data: Python object to serialize.

    Returns:
        Formatted JSON output.
    """
    try:
        return json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
            default=_json_default,
        )
    except TypeError:
        return json.dumps(
            str(data),
            ensure_ascii=False,
            indent=4,
        )


def get_datetime_now_string() -> str:
    """Return the current local datetime as ``YYYYMMDDHHMMSS``."""
    return timezone.localtime().strftime("%Y%m%d%H%M%S")


def get_admin_user() -> User | None:
    """Return the admin user.

    Returns:
        The first user with username ``admin`` or ``None``.
    """
    return User.objects.filter(username="admin").first()


def generate_password(length: int = 16) -> str:
    """Generate a secure random password.

    Args:
        length: Password length.

    Returns:
        Generated password string.

    Raises:
        ValueError: If length is less than 12.
    """
    if length < 12:
        raise ValueError("Password length must be at least 12")

    alphabet = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + "!@#$%^&*()-_=+"
    )

    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_lorem_ipsum_paragraph() -> str:
    """Return one lorem ipsum paragraph."""
    return paragraphs(1)
