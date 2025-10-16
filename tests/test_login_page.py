"""Tests for Login Page functionality"""

import pytest
from pages.login_page import LoginPage


@pytest.mark.login
def test_login_page_with_pom(page, base_url, test_user):
    """Test login using Page Object Model"""
    login_page = LoginPage(page, base_url)
    
    # Navigate to login page
    login_page.navigate_to_login()
    
    # Perform login
    login_page.login(test_user["username"], test_user["password"])
    
    # Note: This is a demo test - actual assertions depend on your app
    # Example: assert login_page.is_error_displayed() == False


@pytest.mark.login
@pytest.mark.negative
def test_login_with_invalid_credentials(page, base_url):
    """Test login with invalid credentials"""
    login_page = LoginPage(page, base_url)
    
    login_page.navigate_to_login()
    login_page.login("invalid@example.com", "wrongpassword")
    
    # Note: Add assertion based on your app's error handling
    # Example: assert login_page.is_error_displayed()


@pytest.mark.login
@pytest.mark.negative
def test_login_with_empty_fields(page, base_url):
    """Test login with empty fields"""
    login_page = LoginPage(page, base_url)
    
    login_page.navigate_to_login()
    login_page.login("", "")
    
    # Note: Add assertion for validation message
    # Example: assert login_page.get_error_message() != ""

