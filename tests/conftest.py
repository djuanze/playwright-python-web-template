"""Pytest configuration and fixtures"""

import os
import pytest
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("BASE_URL", "https://example.com")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

# Create directories for artifacts
SCREENSHOTS_DIR = Path("screenshots")
VIDEOS_DIR = Path("videos")
SCREENSHOTS_DIR.mkdir(exist_ok=True)
VIDEOS_DIR.mkdir(exist_ok=True)


# Hook to capture test result for screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def page(page):
    """
    Override pytest-playwright's page fixture to add custom behavior
    Uses the built-in 'page' fixture from pytest-playwright
    """
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    # Page cleanup is handled by pytest-playwright


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page):
    """Take screenshot on test failure"""
    yield
    
    # Check if test failed and screenshot is enabled
    if SCREENSHOT_ON_FAILURE and hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"
        try:
            page.screenshot(path=str(screenshot_path))
            print(f"\n📸 Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"\n⚠️ Could not save screenshot: {e}")


@pytest.fixture(scope="session")
def base_url():
    """Provide base URL to tests"""
    return BASE_URL


@pytest.fixture(scope="session")
def test_user():
    """Provide test user credentials"""
    return {
        "username": os.getenv("TEST_USERNAME", "demo@example.com"),
        "password": os.getenv("TEST_PASSWORD", "demopass")
    }
