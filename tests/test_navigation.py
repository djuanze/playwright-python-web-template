"""Tests for navigation and page interactions"""

import pytest


@pytest.mark.smoke
def test_page_navigation(page, base_url):
    """Test basic page navigation"""
    page.goto(base_url)
    
    # Verify page loaded
    assert page.url == base_url or page.url == f"{base_url}/"


@pytest.mark.smoke
def test_page_has_content(page, base_url):
    """Test that page has visible content"""
    page.goto(base_url)
    
    # Wait for content to load
    page.wait_for_load_state("domcontentloaded")
    
    # Check that body has content
    body_text = page.locator("body").inner_text()
    assert len(body_text) > 0, "Page should have visible content"


def test_page_back_navigation(page, base_url):
    """Test browser back navigation"""
    page.goto(base_url)
    initial_url = page.url
    
    # Navigate to another page (if available)
    # For demo, we'll just verify current state
    page.go_back()
    
    # Should stay on same page if no history
    assert page.url == initial_url


def test_page_reload(page, base_url):
    """Test page reload functionality"""
    page.goto(base_url)
    initial_title = page.title()
    
    page.reload()
    
    # Title should remain the same after reload
    assert page.title() == initial_title


@pytest.mark.smoke
def test_page_screenshot(page, base_url):
    """Test taking a screenshot"""
    page.goto(base_url)
    
    # Take screenshot
    screenshot_path = "screenshots/test_screenshot.png"
    page.screenshot(path=screenshot_path)
    
    # Verify screenshot was created
    from pathlib import Path
    assert Path(screenshot_path).exists()

