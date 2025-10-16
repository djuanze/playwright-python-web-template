"""Tests for form interactions and validations"""

import pytest


@pytest.mark.skip(reason="Demo test - requires actual forms")
@pytest.mark.forms
def test_input_field_accepts_text(page, base_url):
    """
    Test that input fields accept text - skipped by default
    Remove @pytest.mark.skip to run on a real application
    """
    page.goto(base_url)
    
    # Example: Test any input field on the page
    if page.locator('input[type="text"]').count() > 0:
        input_field = page.locator('input[type="text"]').first
        input_field.fill("Test Text")
        assert input_field.input_value() == "Test Text"


@pytest.mark.skip(reason="Demo test - requires actual forms")
@pytest.mark.forms
def test_form_submission(page, base_url):
    """
    Test form submission behavior - skipped by default
    Remove @pytest.mark.skip to run on a real application
    """
    page.goto(base_url)
    
    # This is a template - customize based on your app
    # Example form interaction:
    # page.fill("#name", "John Doe")
    # page.fill("#email", "john@example.com")
    # page.click("button[type='submit']")
    # page.wait_for_url("**/success")


@pytest.mark.skip(reason="Demo test - requires actual forms")
@pytest.mark.forms
@pytest.mark.negative
def test_form_validation_errors(page, base_url):
    """
    Test that form validation errors display correctly - skipped by default
    Remove @pytest.mark.skip to run on a real application
    """
    page.goto(base_url)
    
    # Template for testing validation
    # Submit empty form and check for validation messages
    # page.click("button[type='submit']")
    # assert page.locator(".error").is_visible()
