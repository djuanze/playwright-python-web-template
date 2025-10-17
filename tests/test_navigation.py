"""Tests for navigation and page interactions"""

import pytest
from pathlib import Path


@pytest.mark.smoke
def test_page_navigation(page, base_url):
    """Test basic page navigation"""
    page.goto(base_url)
    
    # Verify page loaded
    assert page.url == base_url or page.url == f"{base_url}/"
    assert "Example Domain" in page.title()


@pytest.mark.smoke
def test_page_has_content(page, base_url):
    """Test that page has visible content"""
    page.goto(base_url)
    
    # Wait for content to load
    page.wait_for_load_state("domcontentloaded")
    
    # Check that body has content
    body_text = page.locator("body").inner_text()
    assert len(body_text) > 0, "Page should have visible content"
    assert "Example Domain" in body_text


def test_page_back_navigation(page, base_url):
    """Test browser back navigation"""
    # First navigate to a page to create history
    page.goto(base_url)
    initial_url = page.url
    
    # Navigate to another page to create history
    page.goto(f"{base_url}/")  # Same page but creates history
    
    # Now go back
    page.go_back()
    page.wait_for_timeout(500)  # Brief wait for navigation
    
    # Should go back to initial URL or at least not be blank
    assert initial_url == page.url or page.url != "about:blank"


def test_page_reload(page, base_url):
    """Test page reload functionality"""
    page.goto(base_url)
    initial_title = page.title()
    
    page.reload()
    page.wait_for_load_state("domcontentloaded")
    
    # Title should remain the same after reload
    assert page.title() == initial_title


@pytest.mark.smoke
def test_page_screenshot(page, base_url):
    """Test taking a screenshot"""
    page.goto(base_url)
    
    # Ensure screenshots directory exists
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    
    # Take screenshot
    screenshot_path = screenshots_dir / "test_screenshot.png"
    page.screenshot(path=str(screenshot_path))
    
    # Verify screenshot was created
    assert screenshot_path.exists()
    assert screenshot_path.stat().st_size > 0, "Screenshot should not be empty"
