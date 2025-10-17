"""Tests for TestShop BUGGY versions - These tests SHOULD FAIL to verify test validity"""

import pytest
import os

# Point to BUGGY version (Note: Buggy version not deployed to GitHub Pages)
# These tests will be skipped in CI since buggy version is not publicly available
BUGGY_SITE_URL = "file:///Users/reymartjuance/Documents/Myprofile/test-ecommerce-site/bugs"

# Skip bug validation tests in CI since buggy version is not publicly deployed
pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Buggy version not publicly available - run locally for bug validation"
)


@pytest.mark.bug_validation
class TestBuggyVersionValidation:
    """
    These tests run against INTENTIONALLY BROKEN versions of the site.
    
    Expected: Most tests should FAIL (that's good - means tests catch bugs!)
    Purpose: Verify that tests actually detect problems
    """
    
    def test_BUG1_login_accepts_any_password(self, page):
        """
        BUG: Login accepts ANY password as long as email matches
        EXPECTED: This test should PASS (catches the bug)
        """
        page.goto(f"{BUGGY_SITE_URL}/login.html")
        
        # Try login with correct email but WRONG password
        page.fill("#email", "test@testshop.com")
        page.fill("#password", "COMPLETELY_WRONG_PASSWORD")
        page.click("button[type='submit']")
        
        # Wait for potential redirect
        page.wait_for_timeout(2000)
        
        # BUG: Should NOT redirect (wrong password!)
        # But buggy version WILL redirect (accepts any password)
        assert "products.html" in page.url, "BUG DETECTED: Login accepted wrong password!"
        print("✓ BUG CONFIRMED: Login accepts any password (security issue!)")
    
    def test_BUG2_signup_ignores_password_mismatch(self, page):
        """
        BUG: Signup doesn't validate password confirmation
        EXPECTED: This test should PASS (catches bug - no error shown)
        """
        page.goto(f"{BUGGY_SITE_URL}/signup.html")
        
        import time
        timestamp = int(time.time())
        
        # Fill with MISMATCHED passwords
        page.fill("#name", "Test User")
        page.fill("#email", f"bug{timestamp}@test.com")
        page.fill("#password", "Password123!")
        page.fill("#confirm-password", "DIFFERENT_PASSWORD_456!")
        page.check("#terms")
        page.click("button[type='submit']")
        
        page.wait_for_timeout(1000)
        
        # BUG: Should show error, but buggy version shows success!
        success_div = page.locator("#signup-success")
        assert success_div.is_visible(), "BUG DETECTED: Signup succeeded with mismatched passwords!"
        print("✓ BUG CONFIRMED: Signup accepts mismatched passwords (validation broken!)")
    
    def test_BUG3_add_to_cart_doesnt_update_count(self, page):
        """
        BUG: Adding to cart doesn't update cart count in header
        EXPECTED: This test should FAIL (count stays 0)
        """
        page.goto(f"{BUGGY_SITE_URL}/products.html")
        
        initial_count = page.locator("#cart-count").text_content()
        
        # Handle alert
        page.on("dialog", lambda dialog: dialog.accept())
        
        # Add product
        page.locator(".btn-primary").first.click()
        page.wait_for_timeout(500)
        
        current_count = page.locator("#cart-count").text_content()
        
        # BUG: Count should increase but doesn't!
        try:
            assert int(current_count) > int(initial_count)
            print(f"❌ UNEXPECTED: Cart count updated ({initial_count} → {current_count})")
        except AssertionError:
            print(f"✓ BUG CONFIRMED: Cart count NOT updated (stays at {current_count}) - bug detected!")
            raise  # Re-raise to mark test as failed
    
    def test_BUG4_search_returns_nothing(self, page):
        """
        BUG: Search always returns 0 results
        EXPECTED: This test should FAIL (no results found)
        """
        page.goto(f"{BUGGY_SITE_URL}/products.html")
        
        # Search for something that should exist
        page.fill("#search-input", "laptop")
        page.click("text=Search")
        page.wait_for_timeout(500)
        
        products = page.locator(".product-card")
        count = products.count()
        
        # BUG: Should find products but returns 0!
        try:
            assert count > 0, "Search should return results for 'laptop'"
            print(f"❌ UNEXPECTED: Search returned {count} results")
        except AssertionError:
            print("✓ BUG CONFIRMED: Search returns 0 results (search broken!)")
            raise
    
    def test_BUG5_checkout_works_without_login(self, page):
        """
        BUG: Checkout doesn't require authentication
        EXPECTED: This test should FAIL (checkout proceeds without login)
        """
        # Make sure NOT logged in
        page.goto(f"{BUGGY_SITE_URL}/index.html")
        page.evaluate("localStorage.removeItem('currentUser')")
        
        # Add item to cart
        page.goto(f"{BUGGY_SITE_URL}/products.html")
        page.on("dialog", lambda dialog: dialog.accept())
        page.locator(".btn-primary").first.click()
        page.wait_for_timeout(500)
        
        # Go to cart
        page.goto(f"{BUGGY_SITE_URL}/cart.html")
        
        # Try checkout WITHOUT being logged in
        page.evaluate("checkout()")
        page.wait_for_timeout(1000)
        
        # BUG: Should redirect to login, but buggy version allows checkout!
        try:
            assert "login.html" in page.url, "Should redirect to login"
            print("❌ UNEXPECTED: Correctly redirected to login")
        except AssertionError:
            print("✓ BUG CONFIRMED: Checkout works without login (security issue!)")
            raise
    
    def test_BUG6_empty_cart_shows_summary(self, page):
        """
        BUG: Empty cart shows $0.00 summary instead of "empty" message
        EXPECTED: This test should FAIL (wrong UI state)
        """
        # Clear cart
        page.goto(f"{BUGGY_SITE_URL}/index.html")
        page.evaluate("localStorage.removeItem('cart')")
        
        # Go to cart page
        page.goto(f"{BUGGY_SITE_URL}/cart.html")
        page.wait_for_timeout(500)
        
        # BUG: Should show "empty cart" message
        cart_empty = page.locator("#cart-empty")
        cart_summary = page.locator("#cart-summary")
        
        try:
            assert cart_empty.is_visible(), "Should show 'empty cart' message"
            assert not cart_summary.is_visible(), "Should NOT show summary when empty"
            print("❌ UNEXPECTED: Empty cart displays correctly")
        except AssertionError:
            print("✓ BUG CONFIRMED: Empty cart shows summary instead of empty message!")
            raise
    
    def test_BUG7_remove_from_cart_doesnt_refresh(self, page):
        """
        BUG: Removing item from cart doesn't update display
        EXPECTED: This test should FAIL (item still visible)
        """
        # Add item to cart
        page.goto(f"{BUGGY_SITE_URL}/products.html")
        page.on("dialog", lambda dialog: dialog.accept())
        page.locator(".btn-primary").first.click()
        page.wait_for_timeout(500)
        
        # Go to cart
        page.goto(f"{BUGGY_SITE_URL}/cart.html")
        items_before = page.locator(".cart-item").count()
        
        # Remove item
        page.locator(".remove-btn").first.click()
        page.wait_for_timeout(500)
        
        # BUG: Item should disappear but doesn't!
        items_after = page.locator(".cart-item").count()
        
        try:
            assert items_after < items_before, "Item should be removed from display"
            print(f"❌ UNEXPECTED: Item removed correctly ({items_before} → {items_after})")
        except AssertionError:
            print(f"✓ BUG CONFIRMED: Item still visible after removal! ({items_before} → {items_after})")
            raise


# Summary test that shows all bugs
@pytest.mark.bug_validation
def test_SUMMARY_all_bugs_detected(page):
    """
    Summary: This test documents all bugs found
    This test always PASSES to show summary of what was tested
    """
    print("\n" + "="*70)
    print("🐛 BUG VALIDATION SUMMARY")
    print("="*70)
    print("\nThe following bugs were intentionally created for test validation:\n")
    
    bugs = [
        ("BUG #1", "Login accepts ANY password", "CRITICAL SECURITY ISSUE"),
        ("BUG #2", "Signup ignores password mismatch", "Validation broken"),
        ("BUG #3", "Cart count doesn't update", "UX issue"),
        ("BUG #4", "Search returns nothing", "Feature broken"),
        ("BUG #5", "Checkout without login", "SECURITY ISSUE"),
        ("BUG #6", "Empty cart shows summary", "UX issue"),
        ("BUG #7", "Remove doesn't refresh display", "UX issue"),
    ]
    
    for bug_id, description, severity in bugs:
        print(f"{bug_id}: {description}")
        print(f"         Severity: {severity}")
        print()
    
    print("="*70)
    print("✓ All bugs were intentionally created to verify test effectiveness")
    print("✓ Tests that FAIL above are GOOD - they caught the bugs!")
    print("="*70 + "\n")
    
    assert True  # Always pass to show summary

