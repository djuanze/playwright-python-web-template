"""Test data management"""

from typing import Dict, Any


class TestData:
    """Centralized test data"""
    
    # Valid test users
    VALID_USERS = [
        {
            "email": "testuser1@example.com",
            "password": "ValidPass123!",
            "name": "Test User One"
        },
        {
            "email": "testuser2@example.com",
            "password": "ValidPass456!",
            "name": "Test User Two"
        }
    ]
    
    # Invalid credentials for negative testing
    INVALID_CREDENTIALS = [
        {
            "email": "invalid@example.com",
            "password": "wrongpassword",
            "expected_error": "Invalid credentials"
        },
        {
            "email": "notanemail",
            "password": "password123",
            "expected_error": "Invalid email format"
        },
        {
            "email": "",
            "password": "",
            "expected_error": "Email is required"
        }
    ]
    
    # Test URLs
    URLS = {
        "login": "/login",
        "signup": "/signup",
        "dashboard": "/dashboard",
        "profile": "/profile",
        "settings": "/settings"
    }
    
    # Form data
    CONTACT_FORM = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Test Inquiry",
        "message": "This is a test message for automation testing."
    }
    
    # Search queries
    SEARCH_QUERIES = {
        "valid": ["test", "example", "demo"],
        "special_chars": ["test@123", "hello#world", "test & trial"],
        "long_query": "a" * 200,
        "empty": ""
    }
    
    # Browser viewports
    VIEWPORTS = {
        "mobile": {"width": 375, "height": 667},  # iPhone SE
        "tablet": {"width": 768, "height": 1024},  # iPad
        "desktop": {"width": 1920, "height": 1080},  # Full HD
        "4k": {"width": 3840, "height": 2160}  # 4K
    }


def get_test_user(index: int = 0) -> Dict[str, str]:
    """Get a test user by index"""
    return TestData.VALID_USERS[index]


def get_invalid_credential(index: int = 0) -> Dict[str, str]:
    """Get invalid credentials by index"""
    return TestData.INVALID_CREDENTIALS[index]


def get_url(page_name: str) -> str:
    """Get URL for a specific page"""
    return TestData.URLS.get(page_name, "/")


def get_viewport(device: str) -> Dict[str, int]:
    """Get viewport dimensions for a device"""
    return TestData.VIEWPORTS.get(device, TestData.VIEWPORTS["desktop"])

