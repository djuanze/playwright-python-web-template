"""Tests for responsive design and mobile views"""

import pytest


@pytest.mark.mobile
def test_mobile_viewport(page, base_url):
    """Test page on mobile viewport"""
    # Set mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})  # iPhone SE
    page.goto(base_url)
    
    # Verify page loads on mobile
    assert page.title() != ""


@pytest.mark.mobile
def test_tablet_viewport(page, base_url):
    """Test page on tablet viewport"""
    # Set tablet viewport
    page.set_viewport_size({"width": 768, "height": 1024})  # iPad
    page.goto(base_url)
    
    # Verify page loads on tablet
    assert page.title() != ""


@pytest.mark.mobile
def test_desktop_viewport(page, base_url):
    """Test page on desktop viewport"""
    # Set desktop viewport
    page.set_viewport_size({"width": 1920, "height": 1080})  # Full HD
    page.goto(base_url)
    
    # Verify page loads on desktop
    assert page.title() != ""


@pytest.mark.mobile
def test_responsive_elements(page, base_url):
    """Test that elements adapt to different screen sizes"""
    page.goto(base_url)
    
    # Desktop view
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.wait_for_load_state("networkidle")
    
    # Mobile view
    page.set_viewport_size({"width": 375, "height": 667})
    page.wait_for_load_state("networkidle")
    
    # Page should still be functional
    assert page.locator("body").is_visible()

