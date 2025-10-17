"""Demo test to see the browser in action - KEEPS BROWSER OPEN!"""

import pytest
import os
from pages.outfittery_home_page import OutfitteryHomePage

# Skip demo tests in CI since they require specific URLs
pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Demo tests require specific URLs not available in CI"
)


def test_see_browser_in_action(page, base_url):
    """
    This test will open the browser and PAUSE so you can see it!
    Click 'Resume' in the Playwright Inspector to continue.
    """
    print("\n" + "="*60)
    print("🎬 BROWSER WILL OPEN NOW - WATCH YOUR SCREEN!")
    print("="*60)
    
    # Create page object
    home = OutfitteryHomePage(page, base_url)
    
    # Navigate to Outfittery
    print("📍 Navigating to Outfittery.com...")
    home.navigate_to_home()
    
    # Accept cookies
    print("🍪 Accepting cookies...")
    home.accept_cookies()
    
    # PAUSE HERE - Browser will stay open!
    print("\n" + "="*60)
    print("⏸️  BROWSER IS OPEN - LOOK AT YOUR SCREEN!")
    print("⏸️  Click 'Resume' in Playwright Inspector to continue")
    print("="*60)
    page.pause()  # This keeps browser open until you click Resume
    
    # Verify page loaded
    assert page.url.startswith(base_url)
    print("✅ Test passed!")

