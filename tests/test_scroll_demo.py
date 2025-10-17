"""Demo test to SEE the scrolling in action"""

import pytest
import os
from pages.outfittery_home_page import OutfitteryHomePage

# Skip scroll demo tests in CI since they require specific URLs
pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Scroll demo tests require specific URLs not available in CI"
)


def test_see_scroll_slowly(page, base_url):
    """Test scrolling with VISIBLE smooth animation"""
    print("\n🎬 Watch the browser window - it will scroll slowly!\n")
    
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Wait so you can see the page first
    print("⏳ Showing full page for 2 seconds...")
    page.wait_for_timeout(2000)
    
    # Scroll slowly with smooth animation
    print("📜 Starting SMOOTH scroll to footer...")
    page.evaluate("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'  // This makes it scroll smoothly!
        });
    """)
    
    # Wait to watch the scroll happen
    print("👀 Scrolling... (watch the browser!)")
    page.wait_for_timeout(3000)  # Give time to watch scroll
    
    # Verify footer is visible
    footer = page.locator("footer, [role='contentinfo']").first
    assert footer.is_visible(), "Footer should be visible after scrolling"
    
    print("✅ Footer reached! Keeping page open for 3 more seconds...")
    page.wait_for_timeout(3000)
    
    print("✓ Test complete!")


def test_scroll_step_by_step(page, base_url):
    """Scroll in multiple steps so you can see it clearly"""
    print("\n🎬 Watch - scrolling in 5 steps!\n")
    
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    print("Starting at top...")
    page.wait_for_timeout(2000)
    
    # Get page height
    page_height = page.evaluate("document.body.scrollHeight")
    steps = 5
    
    # Scroll in steps
    for i in range(1, steps + 1):
        scroll_to = (page_height * i) // steps
        print(f"📜 Step {i}/{steps}: Scrolling to position {scroll_to}...")
        
        page.evaluate(f"""
            window.scrollTo({{
                top: {scroll_to},
                behavior: 'smooth'
            }});
        """)
        
        page.wait_for_timeout(1500)  # Pause between steps
    
    print("✅ Reached bottom!")
    page.wait_for_timeout(2000)
    
    # Verify footer
    footer = page.locator("footer, [role='contentinfo']").first
    assert footer.is_visible()
    print("✓ Footer is visible!")

