# 🎭 Playwright (Python) Web Template

A **professional, production-ready** Playwright (Python) test automation framework with pytest, Page Object Model, and GitHub Actions CI/CD.

[![pytest](https://img.shields.io/badge/tests-pytest-blue)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Python-success)](https://playwright.dev/python/)
[![CI](https://github.com/djuanze/playwright-python-web-template/actions/workflows/ci.yml/badge.svg)](https://github.com/djuanze/playwright-python-web-template/actions)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## ✨ Features

- ✅ **Page Object Model (POM)** - Maintainable test architecture
- ✅ **Advanced Fixtures** - Screenshots on failure, video recording
- ✅ **Multi-Browser Support** - Test across Chromium, Firefox, WebKit
- ✅ **Responsive Testing** - Mobile, tablet, desktop viewports
- ✅ **GitHub Actions CI/CD** - Automated testing on every push
- ✅ **HTML Reports** - Beautiful test execution reports
- ✅ **Test Markers** - Organize tests (smoke, regression, etc.)
- ✅ **Utilities & Helpers** - Reusable test functions
- ✅ **Environment Config** - Easy configuration via `.env` file

---

## 📁 Project Structure

```
playwright-python-web-template/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                 # GitHub Actions workflow
│   └── ISSUE_TEMPLATE/            # Issue templates
├── pages/                          # Page Object Model
│   ├── __init__.py
│   ├── base_page.py               # Base page class
│   ├── home_page.py               # Home page objects
│   └── login_page.py              # Login page objects
├── tests/                          # Test files
│   ├── conftest.py                # Pytest fixtures & config
│   ├── test_example_smoke.py     # Basic smoke tests
│   ├── test_home_page.py         # Home page tests
│   ├── test_login_page.py        # Login tests (with POM)
│   ├── test_forms.py             # Form interaction tests
│   ├── test_navigation.py        # Navigation tests
│   └── test_responsive.py        # Responsive/mobile tests
├── utils/                          # Helper utilities
│   ├── __init__.py
│   ├── helpers.py                 # Reusable helper functions
│   └── test_data.py               # Centralized test data
├── screenshots/                    # Auto-generated screenshots
├── videos/                         # Auto-generated videos
├── reports/                        # Test reports
├── .gitignore                      # Git ignore file
├── env.example                     # Environment variables template
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── LICENSE                         # MIT License
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/djuanze/playwright-python-web-template.git
cd playwright-python-web-template

# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install --with-deps
```

### 3. Configuration

```bash
# Copy environment template
cp env.example .env

# Edit .env with your settings
nano .env  # or use your preferred editor
```

Example `.env` configuration:
```env
BASE_URL=https://example.com
TEST_USERNAME=demo@example.com
TEST_PASSWORD=demopass
HEADLESS=true
```

### 4. Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_home_page.py

# Run tests with specific marker
pytest -m smoke          # Run only smoke tests
pytest -m login          # Run only login tests
pytest -m "not slow"     # Skip slow tests

# Run tests in parallel (requires pytest-xdist)
pytest -n 4              # Run with 4 workers

# Run with verbose output
pytest -v

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

### 5. View Reports

```bash
# Open HTML report
open reports/report.html      # macOS
start reports/report.html     # Windows
xdg-open reports/report.html  # Linux
```

---

## 🧪 Test Examples

### Basic Test
```python
def test_homepage_loads(page, base_url):
    """Test that homepage loads successfully"""
    page.goto(base_url)
    assert "Example Domain" in page.title()
```

### Using Page Object Model
```python
from pages.login_page import LoginPage

def test_login_with_pom(page, base_url, test_user):
    """Test login using Page Object Model"""
    login_page = LoginPage(page, base_url)
    login_page.navigate_to_login()
    login_page.login(test_user["username"], test_user["password"])
```

### Responsive Testing
```python
@pytest.mark.mobile
def test_mobile_viewport(page, base_url):
    """Test page on mobile viewport"""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(base_url)
    assert page.title() != ""
```

---

## 🏷️ Test Markers

Organize and filter tests using markers:

| Marker | Description |
|--------|-------------|
| `@pytest.mark.smoke` | Critical smoke tests |
| `@pytest.mark.regression` | Full regression suite |
| `@pytest.mark.login` | Login-related tests |
| `@pytest.mark.forms` | Form interaction tests |
| `@pytest.mark.mobile` | Mobile/responsive tests |
| `@pytest.mark.negative` | Negative test scenarios |
| `@pytest.mark.slow` | Tests that take longer |

**Usage:**
```bash
pytest -m smoke                    # Run smoke tests only
pytest -m "smoke or regression"    # Run smoke OR regression
pytest -m "not slow"               # Exclude slow tests
```

---

## 🔧 Advanced Configuration

### Multi-Browser Testing

Run tests across multiple browsers:

```python
@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_cross_browser(browser_name, playwright_instance):
    browser = getattr(playwright_instance, browser_name).launch()
    page = browser.new_page()
    page.goto("https://example.com")
    browser.close()
```

### Screenshots on Failure

Automatically enabled in `conftest.py`. Screenshots saved to `screenshots/` folder.

### Video Recording

Configure in `conftest.py`:
```python
browser_context_args = {
    "record_video_dir": "videos/",
}
```

### Custom Timeouts

```python
# Set default timeout for all actions
page.set_default_timeout(10000)  # 10 seconds

# Set specific timeout for an action
page.click("button", timeout=5000)  # 5 seconds
```

---

## 🎯 Page Object Model

Create maintainable tests using POM:

### 1. Create Page Object

```python
# pages/checkout_page.py
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    PAYMENT_BUTTON = 'button[type="submit"]'
    
    def complete_checkout(self):
        self.click(self.PAYMENT_BUTTON)
```

### 2. Use in Tests

```python
from pages.checkout_page import CheckoutPage

def test_checkout(page, base_url):
    checkout = CheckoutPage(page, base_url)
    checkout.complete_checkout()
```

---

## 📊 Continuous Integration

### GitHub Actions

Tests automatically run on:
- ✅ Push to `main` branch
- ✅ Pull requests
- ✅ Manual workflow dispatch

**Setup GitHub Secrets:**

1. Go to: `Settings` → `Secrets and variables` → `Actions`
2. Add secrets:
   - `BASE_URL`
   - `TEST_USERNAME`
   - `TEST_PASSWORD`

---

## 🛠️ Utilities & Helpers

### Helper Functions

```python
from utils.helpers import generate_random_email, wait_for_page_load

# Generate test data
email = generate_random_email()

# Wait for page to load
wait_for_page_load(page)
```

### Test Data Management

```python
from utils.test_data import get_test_user, get_viewport

# Get predefined test user
user = get_test_user(0)

# Get viewport dimensions
mobile_viewport = get_viewport("mobile")
page.set_viewport_size(mobile_viewport)
```

---

## 📝 Writing Tests

### Best Practices

1. **Use Page Objects** - Keep locators separate from tests
2. **Use Fixtures** - Reuse setup/teardown code
3. **Use Markers** - Organize tests by category
4. **Descriptive Names** - Use clear test function names
5. **Single Responsibility** - One assertion per test (when possible)
6. **Independent Tests** - Tests should not depend on each other

### Example Test Structure

```python
@pytest.mark.smoke
def test_user_can_login(page, base_url, test_user):
    """
    Test that a valid user can log in successfully
    
    Steps:
    1. Navigate to login page
    2. Enter valid credentials
    3. Click login button
    4. Verify redirect to dashboard
    """
    # Arrange
    login_page = LoginPage(page, base_url)
    
    # Act
    login_page.navigate_to_login()
    login_page.login(test_user["username"], test_user["password"])
    
    # Assert
    assert "/dashboard" in page.url
```

---

## 🐛 Debugging

### Run Tests in Headed Mode

```bash
# Edit .env file
HEADLESS=false

# Or set environment variable
HEADLESS=false pytest tests/
```

### Slow Down Test Execution

```bash
# Edit .env file
SLOWMO=1000  # 1 second delay between actions
```

### Use Playwright Inspector

```bash
# Run with inspector
PWDEBUG=1 pytest tests/test_home_page.py
```

### View Screenshots

```bash
# Screenshots saved on test failure
ls screenshots/
```

---

## 📦 Dependencies

See `requirements.txt`:

```txt
pytest==8.3.2
pytest-playwright==0.5.7
playwright==1.48.0
pytest-html==4.1.1
python-dotenv==1.0.1
```

### Optional Dependencies

```bash
# For parallel execution
pip install pytest-xdist

# For better test reporting
pip install pytest-allure
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📚 Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 👤 Author

**Reymart Juance**
- GitHub: [@djuanze](https://github.com/djuanze)
- Location: Philippines

---

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/)
- Testing framework: [pytest](https://pytest.org/)
- Inspired by QA best practices and design patterns

---

**⭐ Star this repo if you find it helpful!**
