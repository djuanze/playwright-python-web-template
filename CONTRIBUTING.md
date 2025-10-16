# Contributing to Playwright Python Web Template

Thank you for considering contributing to this project! 🎉

## How to Contribute

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/playwright-python-web-template.git
cd playwright-python-web-template
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
python -m playwright install --with-deps
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Make Your Changes

- Write clear, descriptive commit messages
- Follow the existing code style
- Add tests for new features
- Update documentation as needed

### 5. Run Tests

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_your_new_feature.py
```

### 6. Submit Pull Request

```bash
git add .
git commit -m "Add: Your feature description"
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

## Code Style Guidelines

### Python Code
- Follow PEP 8 style guide
- Use descriptive variable and function names
- Add docstrings to classes and functions
- Keep functions small and focused

### Test Code
- Use clear test names that describe what's being tested
- Follow Arrange-Act-Assert pattern
- One assertion per test (when reasonable)
- Use appropriate test markers

### Page Objects
- Keep locators as class constants
- Use descriptive locator names
- Inherit from `BasePage`
- Document complex interactions

## Adding New Tests

```python
@pytest.mark.your_marker
def test_descriptive_name(page, base_url):
    """
    Brief description of what this test does
    
    Steps:
    1. Step one
    2. Step two
    3. Step three
    """
    # Arrange
    # Setup code
    
    # Act
    # Perform actions
    
    # Assert
    # Verify results
    assert condition
```

## Adding New Page Objects

```python
from pages.base_page import BasePage

class YourPage(BasePage):
    """Page Object for Your Page"""
    
    # Locators
    ELEMENT_SELECTOR = 'selector'
    
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
    
    def your_method(self):
        """Description of what this method does"""
        self.click(self.ELEMENT_SELECTOR)
```

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the codebase

Thank you for contributing! 🚀

