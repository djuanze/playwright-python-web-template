import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("BASE_URL", "https://example.com")

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture()
def page(browser_context):
    page = browser_context.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()

