class BaseTestCaseMixin:
    """Base test case for shared Django test behavior."""

    @classmethod
    def setUpTestData(cls):
        """Load model metadata and permissions for test assertions."""
        super().setUpTestData()
