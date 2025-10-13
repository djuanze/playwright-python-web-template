# Playwright (Python) Web Template

A minimal, **client‑ready** Playwright (Python) template with pytest + GitHub Actions.

## 🚀 Quick start
```bash
# 1) Create & activate venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 2) Install deps
pip install -r requirements.txt
python -m playwright install --with-deps

# 3) Run tests
pytest

# 4) HTML report
open report.html  # Windows: start report.html
```

## 🔧 Config via env vars

* `BASE_URL` – target site base url (default: https://example.com)
* `TEST_USERNAME` / `TEST_PASSWORD` – demo creds used in `test_login_flow.py`

## 📦 What's included

* Playwright + pytest setup
* Example smoke and login tests
* HTML report (`report.html`)
* GitHub Actions CI workflow (`.github/workflows/ci.yml`)

## 🏷️ Badges

![pytest](https://img.shields.io/badge/tests-pytest-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-success)
![CI](https://github.com/djuanze/playwright-python-web-template/actions/workflows/ci.yml/badge.svg)

## 📝 License

MIT

