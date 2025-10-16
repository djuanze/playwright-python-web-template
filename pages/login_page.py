"""Login Page Object"""

from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Login Page"""
    
    # Locators
    EMAIL_INPUT = 'input[name="email"], input[type="email"], #email'
    PASSWORD_INPUT = 'input[name="password"], input[type="password"], #password'
    LOGIN_BUTTON = 'button[type="submit"], button:has-text("Sign in"), button:has-text("Login")'
    ERROR_MESSAGE = '.error, .alert-danger, [role="alert"]'
    
    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
    
    def navigate_to_login(self):
        """Navigate to the login page"""
        self.navigate(f"{self.base_url}/login")
    
    def login(self, username: str, password: str):
        """Perform login action"""
        self.page.fill(self.EMAIL_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Get error message text if present"""
        if self.page.locator(self.ERROR_MESSAGE).is_visible():
            return self.page.locator(self.ERROR_MESSAGE).inner_text()
        return ""
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

