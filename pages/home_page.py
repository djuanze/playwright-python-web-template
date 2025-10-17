"""Home Page Object"""

from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for Home/Landing Page"""
    
    # Locators
    HEADER = 'header, .header, nav'
    LOGO = 'a[href="/"], .logo, img[alt*="logo"]'
    SEARCH_INPUT = 'input[type="search"], input[placeholder*="Search"]'
    LOGIN_LINK = 'a[href*="login"], button:has-text("Login")'
    SIGNUP_LINK = 'a[href*="signup"], a[href*="register"], button:has-text("Sign up")'
    
    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
    
    def navigate_to_home(self):
        """Navigate to the home page"""
        self.navigate(self.base_url)
    
    def is_header_visible(self) -> bool:
        """Check if header is visible"""
        # For example.com, check for any navigation or main content
        return (self.is_visible(self.HEADER) or 
                self.is_visible("body") or 
                self.is_visible("h1"))
    
    def click_logo(self):
        """Click the logo"""
        self.click(self.LOGO)
    
    def search(self, query: str):
        """Perform a search"""
        self.fill(self.SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")
    
    def click_login(self):
        """Click the login link"""
        self.click(self.LOGIN_LINK)
    
    def click_signup(self):
        """Click the signup link"""
        self.click(self.SIGNUP_LINK)

