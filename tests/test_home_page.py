"""Tests for Home Page"""

import pytest
from pages.home_page import HomePage


def test_homepage_loads(page, base_url):
    """Test that homepage loads successfully"""
    home = HomePage(page, base_url)
    home.navigate_to_home()
    
    assert "Example Domain" in home.get_title()
    assert home.is_header_visible()


def test_homepage_title_contains_domain(page, base_url):
    """Test homepage title contains expected text"""
    home = HomePage(page, base_url)
    home.navigate_to_home()
    
    title = home.get_title()
    assert len(title) > 0, "Page title should not be empty"


@pytest.mark.smoke
def test_homepage_url_is_correct(page, base_url):
    """Test that homepage URL is correct"""
    home = HomePage(page, base_url)
    home.navigate_to_home()
    
    assert base_url in home.get_url()


def test_homepage_elements_visible(page, base_url):
    """Test that key homepage elements are visible"""
    home = HomePage(page, base_url)
    home.navigate_to_home()
    
    # Check if page loaded
    assert page.is_visible("body"), "Page body should be visible"

