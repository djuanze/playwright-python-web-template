"""Test helper functions and utilities"""

import random
import string
from datetime import datetime
from typing import Dict, Any
from playwright.sync_api import Page


def generate_random_email(domain: str = "test.com") -> str:
    """Generate a random email address for testing"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test_{random_string}@{domain}"


def generate_random_string(length: int = 10) -> str:
    """Generate a random alphanumeric string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_timestamp() -> str:
    """Generate a timestamp string"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def wait_for_page_load(page: Page, timeout: int = 30000):
    """Wait for page to fully load"""
    page.wait_for_load_state("networkidle", timeout=timeout)


def scroll_to_element(page: Page, selector: str):
    """Scroll to an element"""
    page.locator(selector).scroll_into_view_if_needed()


def get_element_attribute(page: Page, selector: str, attribute: str) -> str:
    """Get an element's attribute value"""
    return page.locator(selector).get_attribute(attribute)


def is_element_present(page: Page, selector: str) -> bool:
    """Check if element is present in DOM"""
    return page.locator(selector).count() > 0


def wait_for_element(page: Page, selector: str, timeout: int = 10000):
    """Wait for element to be visible"""
    page.wait_for_selector(selector, state="visible", timeout=timeout)


def take_full_page_screenshot(page: Page, path: str):
    """Take a full page screenshot"""
    page.screenshot(path=path, full_page=True)


def get_local_storage(page: Page, key: str) -> Any:
    """Get value from local storage"""
    return page.evaluate(f"localStorage.getItem('{key}')")


def set_local_storage(page: Page, key: str, value: str):
    """Set value in local storage"""
    page.evaluate(f"localStorage.setItem('{key}', '{value}')")


def clear_local_storage(page: Page):
    """Clear all local storage"""
    page.evaluate("localStorage.clear()")


def get_cookies(page: Page) -> list:
    """Get all cookies"""
    return page.context.cookies()


def clear_cookies(page: Page):
    """Clear all cookies"""
    page.context.clear_cookies()


def hover_element(page: Page, selector: str):
    """Hover over an element"""
    page.locator(selector).hover()


def double_click_element(page: Page, selector: str):
    """Double click an element"""
    page.locator(selector).dblclick()


def right_click_element(page: Page, selector: str):
    """Right click an element"""
    page.locator(selector).click(button="right")


def select_dropdown_option(page: Page, selector: str, value: str):
    """Select dropdown option by value"""
    page.locator(selector).select_option(value)


def upload_file(page: Page, selector: str, file_path: str):
    """Upload a file"""
    page.locator(selector).set_input_files(file_path)


def get_page_console_logs(page: Page) -> list:
    """Collect console logs (must set up listener first)"""
    logs = []
    
    def handle_console(msg):
        logs.append(f"{msg.type}: {msg.text}")
    
    page.on("console", handle_console)
    return logs

