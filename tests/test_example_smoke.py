def test_homepage_title(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()

