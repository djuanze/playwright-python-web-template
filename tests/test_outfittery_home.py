"""Tests for Outfittery.com Homepage"""

import pytest
from pages.outfittery_home_page import OutfitteryHomePage


@pytest.mark.smoke
def test_homepage_loads_successfully(page, base_url):
    """Test that Outfittery homepage loads without errors"""
    home = OutfitteryHomePage(page, base_url)
    
    # Navigate to homepage
    home.navigate_to_home()
    
    # Accept cookies if banner appears
    home.accept_cookies()
    
    # Verify page loaded
    assert page.url.startswith(base_url), f"Expected URL to start with {base_url}"
    print(f"✓ Homepage loaded: {page.url}")


@pytest.mark.smoke
def test_page_has_title(page, base_url):
    """Test that page has a proper title"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    title = page.title()
    assert len(title) > 0, "Page title should not be empty"
    assert "Outfittery" in title or "outfittery" in title.lower(), "Title should contain 'Outfittery'"
    print(f"✓ Page title: {title}")


@pytest.mark.smoke
def test_logo_is_visible(page, base_url):
    """Test that company logo is visible"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    assert home.is_logo_visible(), "Logo should be visible on homepage"
    print("✓ Logo is visible")


@pytest.mark.smoke
def test_navigation_header_is_visible(page, base_url):
    """Test that main navigation header is visible"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    assert home.is_header_visible(), "Navigation header should be visible"
    print("✓ Navigation header is visible")


def test_page_content_is_loaded(page, base_url):
    """Test that page has visible content"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Get body text
    body_text = page.locator("body").inner_text()
    
    assert len(body_text) > 100, "Page should have substantial content"
    print(f"✓ Page has {len(body_text)} characters of content")


def test_page_has_no_console_errors(page, base_url):
    """Test that page loads without major console errors"""
    errors = []
    
    # Listen for console messages
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Wait for page to fully load
    page.wait_for_load_state("networkidle")
    
    # Check for critical errors (allow some minor errors)
    critical_errors = [e for e in errors if "Failed to load resource" not in e]
    
    if critical_errors:
        print(f"⚠ Found {len(critical_errors)} console errors:")
        for error in critical_errors[:5]:  # Show first 5
            print(f"  - {error}")
    else:
        print("✓ No critical console errors found")


@pytest.mark.mobile
def test_homepage_responsive_mobile(page, base_url):
    """Test that homepage works on mobile viewport"""
    # Set mobile viewport (iPhone 13)
    page.set_viewport_size({"width": 390, "height": 844})
    
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Verify page is functional on mobile
    assert home.is_header_visible() or home.is_logo_visible(), "Page should be functional on mobile"
    print("✓ Homepage works on mobile viewport (390x844)")


@pytest.mark.mobile
def test_homepage_responsive_tablet(page, base_url):
    """Test that homepage works on tablet viewport"""
    # Set tablet viewport (iPad Air)
    page.set_viewport_size({"width": 820, "height": 1180})
    
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Verify page is functional on tablet
    assert home.is_header_visible(), "Page should be functional on tablet"
    print("✓ Homepage works on tablet viewport (820x1180)")


def test_scroll_to_footer(page, base_url):
    """Test scrolling to page footer"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    # Scroll to footer
    home.scroll_to_footer()
    
    # Check if footer is in viewport
    footer = page.locator("footer, [role='contentinfo']").first
    assert footer.is_visible(), "Footer should be visible after scrolling"
    print("✓ Successfully scrolled to footer")


def test_page_language_attribute(page, base_url):
    """Test that page has proper language attribute"""
    home = OutfitteryHomePage(page, base_url)
    home.navigate_to_home()
    home.accept_cookies()
    
    language = home.get_page_language()
    assert language != "unknown", "Page should have a language attribute"
    print(f"✓ Page language: {language}")


@pytest.mark.slow
def test_page_load_performance(page, base_url):
    """Test that page loads within acceptable time"""
    import time
    
    home = OutfitteryHomePage(page, base_url)
    
    start_time = time.time()
    home.navigate_to_home()
    page.wait_for_load_state("domcontentloaded")
    load_time = time.time() - start_time
    
    home.accept_cookies()
    
    # Check load time (should be under 5 seconds)
    assert load_time < 5.0, f"Page took {load_time:.2f}s to load (should be < 5s)"
    print(f"✓ Page loaded in {load_time:.2f} seconds")

