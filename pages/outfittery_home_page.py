"""Page Object for Outfittery Homepage"""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class OutfitteryHomePage(BasePage):
    """Page Object for Outfittery.com Homepage"""
    
    # Locators
    HEADER = 'header, nav, [role="navigation"]'
    LOGO = 'a[href="/"], img[alt*="Outfittery"], .logo'
    COOKIE_BANNER = '[class*="cookie"], [id*="cookie"], #onetrust-banner-sdk'
    COOKIE_ACCEPT_BUTTON = 'button:has-text("Accept"), button:has-text("Akzeptieren"), #onetrust-accept-btn-handler'
    
    # Navigation links
    HOW_IT_WORKS_LINK = 'a:has-text("How it works"), a:has-text("Wie es funktioniert")'
    FOR_MEN_LINK = 'a:has-text("For Men"), a:has-text("Für Männer")'
    FOR_WOMEN_LINK = 'a:has-text("For Women"), a:has-text("Für Frauen")'
    
    # Call-to-action buttons
    GET_STARTED_BUTTON = 'button:has-text("Get started"), a:has-text("Get started"), button:has-text("Jetzt starten")'
    
    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.base_url = base_url
    
    def navigate_to_home(self):
        """Navigate to Outfittery homepage"""
        self.navigate(self.base_url)
    
    def accept_cookies(self):
        """Accept cookie banner if present"""
        try:
            # Wait for cookie banner with short timeout
            self.page.wait_for_selector(self.COOKIE_BANNER, timeout=3000)
            
            # Click accept button if visible
            if self.page.locator(self.COOKIE_ACCEPT_BUTTON).is_visible():
                self.page.locator(self.COOKIE_ACCEPT_BUTTON).first.click()
                # Wait for banner to disappear
                self.page.wait_for_timeout(1000)
                print("✓ Cookies accepted")
        except:
            # Cookie banner not present, continue
            print("ℹ No cookie banner found")
            pass
    
    def is_logo_visible(self) -> bool:
        """Check if logo is visible"""
        return self.page.locator(self.LOGO).first.is_visible()
    
    def is_header_visible(self) -> bool:
        """Check if header/navigation is visible"""
        return self.page.locator(self.HEADER).first.is_visible()
    
    def click_how_it_works(self):
        """Click 'How it works' link"""
        self.page.locator(self.HOW_IT_WORKS_LINK).first.click()
    
    def click_for_men(self):
        """Click 'For Men' link"""
        self.page.locator(self.FOR_MEN_LINK).first.click()
    
    def click_for_women(self):
        """Click 'For Women' link"""
        self.page.locator(self.FOR_WOMEN_LINK).first.click()
    
    def click_get_started(self):
        """Click 'Get Started' CTA button"""
        self.page.locator(self.GET_STARTED_BUTTON).first.click()
    
    def scroll_to_footer(self):
        """Scroll to page footer"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(500)
    
    def get_page_language(self) -> str:
        """Get the page language from html tag"""
        return self.page.locator("html").get_attribute("lang") or "unknown"

