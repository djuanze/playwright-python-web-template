"""Base Page Object - Parent class for all page objects"""

from playwright.sync_api import Page, expect


class BasePage:
    """Base page class that all page objects inherit from"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get the page title"""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get the current URL"""
        return self.page.url
    
    def wait_for_url(self, url: str, timeout: int = 10000):
        """Wait for URL to match"""
        self.page.wait_for_url(url, timeout=timeout)
    
    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill a text input"""
        self.page.fill(selector, text)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()
    
    def take_screenshot(self, path: str):
        """Take a screenshot"""
        self.page.screenshot(path=path)

