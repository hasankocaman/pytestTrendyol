# Trendyol MacBook Test Automation

This project is a Selenium-based test automation framework for testing the MacBook purchase flow on Trendyol.com.

## Features

- Page Object Model (POM) design pattern
- Automated logging
- Screenshot capture on failures
- Video recording of test execution
- Chrome WebDriver integration

## Project Structure

```
├── pages/
│   ├── base_page.py
│   └── trendyol_page.py
├── tests/
│   └── test_macbook_purchase.py
├── logs/
├── screenshots/
├── videos/
├── requirements.txt
└── README.md
```

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests:

```bash
pytest tests/test_macbook_purchase.py -v
```

## Output

- Test logs are saved in the `logs` directory
- Screenshots are saved in the `screenshots` directory
- Video recordings are saved in the `videos` directory
