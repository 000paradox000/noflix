import json
import uuid
from pathlib import Path

from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from django.test import TestCase

from noflix.common import utilities

from .base import BaseTestCaseMixin


class UtilitiesTest(BaseTestCaseMixin, TestCase):
    """Tests for utility helpers."""

    def test_get_visitor_ip_without_request(self) -> None:
        """Return localhost when request is missing."""
        self.assertEqual(
            utilities.get_visitor_ip(),
            "127.0.0.1",
        )

    def test_get_visitor_ip_from_remote_addr(self) -> None:
        """Return REMOTE_ADDR when available."""
        request = HttpRequest()
        request.META["REMOTE_ADDR"] = "10.0.0.1"

        self.assertEqual(
            utilities.get_visitor_ip(request),
            "10.0.0.1",
        )

    def test_get_visitor_ip_from_forwarded_for(self) -> None:
        """Return first forwarded IP."""
        request = HttpRequest()
        request.META["HTTP_X_FORWARDED_FOR"] = "203.0.113.1, 10.0.0.1"

        self.assertEqual(
            utilities.get_visitor_ip(request),
            "203.0.113.1",
        )

    def test_create_admin_user(self) -> None:
        """Create a superuser successfully."""
        user = utilities.create_admin_user(
            username="admin2",
            password="secret123",
            first_name="Admin",
            last_name="Two",
            email="admin2@example.com",
        )

        self.assertEqual(user.username, "admin2")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_normal_user(self) -> None:
        """Create a normal user successfully."""
        user = utilities.create_normal_user(
            username="john",
            password="secret123",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
        )

        self.assertEqual(user.username, "john")
        self.assertFalse(user.is_superuser)

    def test_add_user_to_group(self) -> None:
        """Add user to a group."""
        user = User.objects.create_user(
            username="mike",
            password="secret123",
        )

        utilities.add_user_to_group(
            user=user,
            group_name="Editors",
        )

        self.assertTrue(
            user.groups.filter(name="Editors").exists(),
        )
        self.assertTrue(
            Group.objects.filter(name="Editors").exists(),
        )

    def test_user_exists(self) -> None:
        """Return True when user exists."""
        User.objects.create_user(
            username="alice",
            password="secret123",
        )

        self.assertTrue(
            utilities.user_exists("alice"),
        )
        self.assertFalse(
            utilities.user_exists("missing"),
        )

    def test_generate_hash_value(self) -> None:
        """Return a UUID hex string."""
        value = utilities.generate_hash_value()

        self.assertEqual(len(value), 32)
        uuid.UUID(hex=value)

    def test_to_json(self) -> None:
        """Serialize Python data to JSON."""
        data = {
            "name": "john",
            "path": Path("/tmp/demo"),
        }

        result = utilities.to_json(data)

        parsed = json.loads(result)
        self.assertEqual(parsed["name"], "john")
        self.assertEqual(
            parsed["path"],
            "/tmp/demo",
        )

    def test_get_datetime_now_string(self) -> None:
        """Return formatted datetime string."""
        value = utilities.get_datetime_now_string()

        self.assertEqual(len(value), 14)
        self.assertTrue(value.isdigit())

    def test_generate_password(self) -> None:
        """Generate password with requested length."""
        value = utilities.generate_password(16)

        self.assertEqual(len(value), 16)

    def test_generate_password_invalid_length(self) -> None:
        """Raise error when length is too short."""
        with self.assertRaises(ValueError):
            utilities.generate_password(8)

    def test_generate_lorem_ipsum_paragraph(self) -> None:
        """Return lorem ipsum text."""
        value = utilities.generate_lorem_ipsum_paragraph()

        self.assertIsInstance(value, list)
        self.assertTrue(len(value) > 0)
