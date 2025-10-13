import os

USERNAME = os.getenv("TEST_USERNAME", "demo@example.com")
PASSWORD = os.getenv("TEST_PASSWORD", "demopass")
BASE_URL = os.getenv("BASE_URL", "https://example.com")

def test_login_flow(page):
    page.goto(f"{BASE_URL}/login")
    page.get_by_label("Email").fill(USERNAME)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{BASE_URL}/dashboard")
    assert page.url.endswith("/dashboard")

