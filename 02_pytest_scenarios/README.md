# 🧪 Pytest Scenarios

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/) [![Pytest](https://img.shields.io/badge/Pytest-Test%20Automation-orange?logo=pytest)](https://docs.pytest.org/) [![Playwright](https://img.shields.io/badge/Playwright-Browser%20Automation-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)

> **Test organization and execution fundamentals** — practical Pytest scenarios used to structure, execute and validate automated tests.

---

## 🎯 Purpose

This section demonstrates the core Pytest mechanisms used to organize test scenarios, prepare test state, validate results and control execution.

---

## 📚 Topics

### 🧪 Test Functions
Pytest discovers test functions using conventions such as the `test_` prefix. Separate test functions make scenarios easier to identify and maintain.

📄 **Script:** [`test_basic_function.py`](Scripts/test_basic_function.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_basic_function.png)](Screenshots/test_basic_function.png)

---

### ✅ Assertions
Assertions compare actual results with expected results and determine whether a test passes or fails.

📄 **Script:** [`test_assertions.py`](Scripts/test_assertions.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_assertions.png)](Screenshots/test_assertions.png)

---

### 🔧 Fixtures
Fixtures provide reusable setup or test data to test functions.

📄 **Script:** [`test_fixtures.py`](Scripts/test_fixtures.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_fixtures.png)](Screenshots/test_fixtures.png)

---

### 🔄 Setup & Teardown
Setup prepares the test environment and teardown performs required cleanup.

📄 **Script:** [`test_setup_function.py`](Scripts/test_setup_function.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_setup_function.png)](Screenshots/test_setup_function.png)

📄 **Script:** [`test_setup_module.py`](Scripts/test_setup_module.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_setup_module.png)](Screenshots/test_setup_module.png)

---

### 🏷️ Markers
Markers categorize tests so selected groups can be executed independently.

📄 **Script:** [`test_markers.py`](Scripts/test_markers.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_makers.png)](Screenshots/test_makers.png)

---

### 🔢 Test Ordering
Demonstrates ordered execution with `pytest.mark.order`. Independent tests are generally easier to maintain because they do not depend on another test's state.

📄 **Script:** [`test_order.py`](Scripts/test_order.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_order.png)](Screenshots/test_order.png)

---

### 🔁 Parameterization

Runs the same test logic with multiple sets of input data.

Parameterization allows the same test to run with different input values without duplicating the test code.

📄 **Script:** [test_paramater_mark.py](Scripts/test_paramater_mark.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_parameter_mark.png)](Screenshots/test_parameter_mark.png)

---

## ⚙️ Test Configuration

[`pytest.ini`](../pytest.ini) is the project-level Pytest configuration file. It defines test discovery rules, registered markers and default execution options used across the automation project.

It is located at the repository root and applies to the relevant Pytest test suites; it is not a test script specific to this folder.

---

## 🔑 Key Takeaway

These scenarios demonstrate the Pytest mechanisms used to structure reliable automation: test functions, assertions, fixtures, setup/teardown, markers, ordering and parameterized execution.
