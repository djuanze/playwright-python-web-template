"""Pytest configuration and fixtures"""

import os
import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("BASE_URL", "https://example.com")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOWMO = int(os.getenv("SLOWMO", "0"))
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

# Create directories for artifacts
SCREENSHOTS_DIR = Path("screenshots")
VIDEOS_DIR = Path("videos")
SCREENSHOTS_DIR.mkdir(exist_ok=True)
VIDEOS_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments"""
    return {
        "headless": HEADLESS,
        "slow_mo": SLOWMO,
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments"""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": str(VIDEOS_DIR),
    }


@pytest.fixture(scope="session")
def playwright_instance():
    """Create Playwright instance"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_type_launch_args):
    """Launch browser for the session"""
    browser = playwright_instance.chromium.launch(**browser_type_launch_args)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, browser_context_args):
    """Create a new browser context for each test"""
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    """Create a new page for each test with screenshot on failure"""
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)
    
    yield page
    
    # Take screenshot on test failure
    if SCREENSHOT_ON_FAILURE and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"
        page.screenshot(path=str(screenshot_path))
        print(f"\n📸 Screenshot saved: {screenshot_path}")
    
    page.close()


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


# Multi-browser support
@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def multi_browser(playwright_instance, browser_type_launch_args, request):
    """Run tests across multiple browsers"""
    browser_type = getattr(playwright_instance, request.param)
    browser = browser_type.launch(**browser_type_launch_args)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def multi_browser_page(multi_browser, browser_context_args):
    """Create page for multi-browser tests"""
    context = multi_browser.new_context(**browser_context_args)
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    page.close()
    context.close()


# Hook to capture test result for screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
