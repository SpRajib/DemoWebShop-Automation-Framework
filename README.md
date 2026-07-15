# 🛒 Demo Web Shop Automation Framework

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-orange?style=for-the-badge)
![Chrome](https://img.shields.io/badge/Browser-Chrome-success?style=for-the-badge&logo=googlechrome)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**End-to-End Web Automation Testing Framework built using Python, Selenium WebDriver, Pytest, and the Page Object Model (POM).**

</div>

---

# 📌 Project Overview

This project automates the **Demo Web Shop** e-commerce application using a scalable **Page Object Model (POM)** framework.

The framework demonstrates industry-standard automation practices including:

- ✅ Page Object Model (POM)
- ✅ Selenium WebDriver
- ✅ Pytest Framework
- ✅ Explicit Waits
- ✅ Configuration Management
- ✅ HTML Test Reports
- ✅ Screenshot Capture on Failure
- ✅ Logging
- ✅ Reusable Components
- ✅ Clean Project Structure

---

# 🌐 Application Under Test

**Website**

https://demowebshop.tricentis.com/

---

# 🎯 Project Objectives

- Automate critical e-commerce user flows.
- Improve test maintainability using POM.
- Demonstrate reusable automation framework design.
- Generate professional HTML reports.
- Capture screenshots on test failures.
- Showcase Selenium automation best practices.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| WebDriver Manager | Driver Management |
| ConfigParser | Configuration File Handling |
| Logging | Test Logging |
| HTML Reports | Test Execution Reports |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
DemoWebShop-Automation/
│
├── pages/
│   ├── HomePage.py
│   ├── LoginPage.py
│   ├── RegisterPage.py
│   ├── SearchPage.py
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   └── ProductReviewPage.py
│
├── testCases/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_add_to_cart.py
│   ├── test_remove_cart.py
│   ├── test_checkout.py
│   └── test_product_review.py
│
├── utilities/
│   ├── BaseClass.py
│   ├── Logger.py
│   ├── ReadConfig.py
│   └── custom_wait.py
│
├── configuration/
│   └── config.ini
│
├── documentation/
│   ├── TestCases.md
│   └── TestPlan.md
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# ⚙ Features

### ✔ User Registration

- Register new user
- Mandatory field validation
- Duplicate email validation

---

### ✔ Login

- Valid Login
- Invalid Login
- Empty Credentials
- Logout

---

### ✔ Product Search

- Existing Product
- Invalid Product
- Empty Search

---

### ✔ Shopping Cart

- Add Product
- Remove Product
- Verify Cart Count

---

### ✔ Checkout

- Billing Address
- Shipping Method
- Payment Method
- Confirm Order

---

### ✔ Product Review

- Submit Product Review
- Validation Checks
- Rating Selection
- Verify Submitted Review

---

# 🧪 Automated Test Cases

| Module | Test Cases |
|---------|-----------:|
| Registration | 3 |
| Login | 4 |
| Search | 3 |
| Add to Cart | 2 |
| Remove Cart | 2 |
| Checkout | 2 |
| Product Review | 5 |
| **Total** | **21** |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DemoWebShop-Automation.git
```

Move into the project directory

```bash
cd DemoWebShop-Automation
```

Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Tests

Run all tests

```bash
pytest -v
```

Generate HTML Report

```bash
pytest -v --html=reports/report.html
```

Run a specific test

```bash
pytest testCases/test_login.py
```

---

# 📊 Reports

After execution, HTML reports are generated in:

```text
reports/
```

The report contains:

- Test Summary
- Passed Tests
- Failed Tests
- Execution Time
- Failure Details

---

# 📷 Screenshots

Whenever a test fails, screenshots are automatically captured and stored in:

```text
screenshots/
```

This helps quickly identify UI issues and failures.

---

# 🏗 Framework Architecture

```text
Test Cases
      │
      ▼
Page Object Model
      │
      ▼
Utility Layer
      │
      ▼
Selenium WebDriver
      │
      ▼
Demo Web Shop Application
```

---

# 💡 Design Pattern

This framework follows the **Page Object Model (POM)**.

### Advantages

- Reusable code
- Easy maintenance
- Better readability
- Reduced code duplication
- Industry-standard automation architecture

---

# 📈 Future Enhancements

- Jenkins CI/CD Integration
- GitHub Actions Workflow
- Docker Support
- Cross Browser Testing
- Parallel Execution
- Data-Driven Testing
- Allure Reports
- Excel Utility
- Database Validation

---

# 👨‍💻 Author

**Rajib Lochan Sahoo**

MCA Graduate

Python | Selenium | SQL | Automation Testing

GitHub: https://github.com/SpRajib

---

# ⭐ If you found this project useful

Give this repository a ⭐ on GitHub.

It motivates me to build more automation frameworks and open-source projects.