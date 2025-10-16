"""Basic login flow test (legacy format for demo)"""

import os
import pytest

USERNAME = os.getenv("TEST_USERNAME", "demo@example.com")
PASSWORD = os.getenv("TEST_PASSWORD", "demopass")
BASE_URL = os.getenv("BASE_URL", "https://example.com")


@pytest.mark.skip(reason="Demo test - requires actual login page")
def test_login_flow(page):
    """
    Demo test for login flow - skipped by default
    Uncomment @pytest.mark.skip to run on a real application
    """
    page.goto(f"{BASE_URL}/login")
    page.get_by_label("Email").fill(USERNAME)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{BASE_URL}/dashboard")
    assert page.url.endswith("/dashboard")
