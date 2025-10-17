"""Tests for TestShop E-commerce Demo Site"""

import pytest
import os
from playwright.sync_api import expect


# Update BASE_URL to point to your local site
TEST_SITE_URL = "file:///Users/reymartjuance/Documents/Myprofile/test-ecommerce-site"

# Skip all tests in CI environment since TestShop files are not available
pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="TestShop files not available in CI environment"
)


@pytest.mark.smoke
def test_homepage_loads(page):
    """Test that TestShop homepage loads successfully"""
    page.goto(f"{TEST_SITE_URL}/index.html")
    
    # Verify page loaded
    assert "Test Shop" in page.title()
    print("✓ Homepage loaded successfully")


@pytest.mark.smoke
def test_login_with_valid_credentials(page):
    """Test login with valid test credentials"""
    page.goto(f"{TEST_SITE_URL}/login.html")
    
    # Fill login form
    page.fill("#email", "test@testshop.com")
    page.fill("#password", "Test123!")
    
    # Submit form
    page.click("button[type='submit']")
    
    # Wait for redirect
    page.wait_for_timeout(2000)
    
    # Verify redirected to products page
    assert "products.html" in page.url
    print("✓ Login successful with valid credentials")


@pytest.mark.negative
def test_login_with_invalid_credentials(page):
    """Test login with invalid credentials shows error"""
    page.goto(f"{TEST_SITE_URL}/login.html")
    
    # Fill with invalid credentials
    page.fill("#email", "wrong@example.com")
    page.fill("#password", "wrongpass")
    
    # Submit form
    page.click("button[type='submit']")
    
    # Wait for error message
    page.wait_for_timeout(500)
    
    # Verify error message appears
    error_div = page.locator("#login-error")
    assert error_div.is_visible()
    print("✓ Error message displayed for invalid credentials")


@pytest.mark.smoke
def test_signup_creates_new_account(page):
    """Test signup with new account"""
    page.goto(f"{TEST_SITE_URL}/signup.html")
    
    # Generate unique email
    import time
    timestamp = int(time.time())
    email = f"newuser{timestamp}@test.com"
    
    # Fill signup form
    page.fill("#name", "New User")
    page.fill("#email", email)
    page.fill("#password", "NewPass123!")
    page.fill("#confirm-password", "NewPass123!")
    page.check("#terms")
    
    # Submit form
    page.click("button[type='submit']")
    
    # Wait for success message
    page.wait_for_timeout(1000)
    
    # Verify success message
    success_div = page.locator("#signup-success")
    assert success_div.is_visible()
    print(f"✓ Account created successfully for {email}")


@pytest.mark.negative
def test_signup_password_mismatch(page):
    """Test signup shows error when passwords don't match"""
    page.goto(f"{TEST_SITE_URL}/signup.html")
    
    # Fill form with mismatched passwords
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")
    page.fill("#password", "Password123!")
    page.fill("#confirm-password", "DifferentPass123!")
    page.check("#terms")
    
    # Submit form
    page.click("button[type='submit']")
    
    # Wait for error
    page.wait_for_timeout(500)
    
    # Verify error message
    error_div = page.locator("#signup-error")
    assert error_div.is_visible()
    assert "do not match" in error_div.text_content().lower()
    print("✓ Password mismatch error displayed correctly")


def test_product_search(page):
    """Test product search functionality"""
    page.goto(f"{TEST_SITE_URL}/products.html")
    
    # Search for laptop
    page.fill("#search-input", "laptop")
    page.click("text=Search")
    
    # Wait for search results
    page.wait_for_timeout(500)
    
    # Verify laptop is in results
    products = page.locator(".product-card")
    assert products.count() > 0
    print(f"✓ Search returned {products.count()} result(s)")


def test_add_product_to_cart(page):
    """Test adding product to shopping cart"""
    page.goto(f"{TEST_SITE_URL}/products.html")
    
    # Get initial cart count
    cart_count_before = page.locator("#cart-count").text_content()
    
    # Handle alert when adding to cart
    page.on("dialog", lambda dialog: dialog.accept())
    
    # Click first "Add to Cart" button
    page.locator(".btn-primary").first.click()
    
    # Wait for cart to update
    page.wait_for_timeout(500)
    
    # Verify cart count increased
    cart_count_after = page.locator("#cart-count").text_content()
    assert int(cart_count_after) > int(cart_count_before)
    print(f"✓ Product added to cart. Count: {cart_count_before} → {cart_count_after}")


def test_view_cart_with_items(page):
    """Test viewing shopping cart with items"""
    # First add item to cart
    page.goto(f"{TEST_SITE_URL}/products.html")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator(".btn-primary").first.click()
    page.wait_for_timeout(500)
    
    # Navigate to cart
    page.goto(f"{TEST_SITE_URL}/cart.html")
    
    # Verify cart has items
    cart_items = page.locator(".cart-item")
    assert cart_items.count() > 0
    print(f"✓ Cart contains {cart_items.count()} item(s)")
    
    # Verify summary is visible
    assert page.locator("#cart-summary").is_visible()
    print("✓ Cart summary displayed")


def test_remove_item_from_cart(page):
    """Test removing item from shopping cart"""
    # Add item to cart
    page.goto(f"{TEST_SITE_URL}/products.html")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator(".btn-primary").first.click()
    page.wait_for_timeout(500)
    
    # Go to cart
    page.goto(f"{TEST_SITE_URL}/cart.html")
    
    # Get item count before
    items_before = page.locator(".cart-item").count()
    
    # Remove first item
    page.locator(".remove-btn").first.click()
    page.wait_for_timeout(500)
    
    # Verify item removed
    items_after = page.locator(".cart-item").count()
    assert items_after == items_before - 1
    print(f"✓ Item removed. Cart items: {items_before} → {items_after}")


def test_checkout_requires_login(page):
    """Test that checkout requires user to be logged in"""
    # Add item to cart
    page.goto(f"{TEST_SITE_URL}/products.html")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator(".btn-primary").first.click()
    page.wait_for_timeout(500)
    
    # Go to cart and try checkout
    page.goto(f"{TEST_SITE_URL}/cart.html")
    
    # Handle alert
    page.on("dialog", lambda dialog: dialog.accept())
    
    # Click checkout
    page.evaluate("checkout()")
    
    # Wait for redirect
    page.wait_for_timeout(1000)
    
    # Should redirect to login
    assert "login.html" in page.url
    print("✓ Checkout correctly requires login")


@pytest.mark.mobile
def test_site_works_on_mobile(page):
    """Test that site is functional on mobile viewport"""
    # Set mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})
    
    page.goto(f"{TEST_SITE_URL}/index.html")
    
    # Verify key elements are visible
    assert page.locator(".logo").is_visible()
    assert page.locator(".hero").is_visible()
    print("✓ Site works on mobile viewport (375x667)")


def test_navigation_between_pages(page):
    """Test navigation between different pages"""
    # Start at homepage
    page.goto(f"{TEST_SITE_URL}/index.html")
    assert "index.html" in page.url
    
    # Navigate to products
    page.click("text=Products")
    page.wait_for_timeout(500)
    assert "products.html" in page.url
    print("✓ Navigated: Home → Products")
    
    # Navigate to login
    page.click("text=Login")
    page.wait_for_timeout(500)
    assert "login.html" in page.url
    print("✓ Navigated: Products → Login")
    
    # Navigate back to home
    page.click("text=Home")
    page.wait_for_timeout(500)
    assert "index.html" in page.url
    print("✓ Navigated: Login → Home")

