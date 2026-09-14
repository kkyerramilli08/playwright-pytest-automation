# 🎭 Playwright Configuration, Locators & Assertions

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/) [![Pytest](https://img.shields.io/badge/Pytest-Test%20Automation-orange?logo=pytest)](https://docs.pytest.org/) [![Playwright](https://img.shields.io/badge/Playwright-Browser%20Automation-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)

> **Element identification + validation** — Playwright configuration, locator strategies and assertion-based browser validation.

---

## 🎯 Purpose

This section demonstrates how Playwright identifies elements, interacts with web pages and validates application state.

---

## 📚 Topics

### ⚙️ Playwright Configuration

Playwright is configured to run browser-based tests through Pytest. The project-level `pytest.ini` controls browser execution options such as the Chromium browser and headed execution.

📄 **Configuration:** [`pytest.ini`](../pytest.ini)

📄 **Example Script:** [`test_example.py`](Scripts/test_example.py)

The `test_example.py` script demonstrates the basic Playwright test setup and browser interaction used in this section.

#### 📸 Output
[![Execution Evidence](Screenshots/test_example.png)](Screenshots/test_example.png)

---

### 🔹 get_by_role()
Semantic role-based element identification.

📄 **Script:** [`test_getbyrole.py`](Scripts/test_getbyrole.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbyrole.png)](Screenshots/test_getbyrole.png)

---
### 🔹 get_by_text()
Locating elements by visible text.

📄 **Script:** [`test_getbytext.py`](Scripts/test_getbytext.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbytext.png)](Screenshots/test_getbytext.png)

---
### 🔹 get_by_label()
Locating form controls through their associated labels.

📄 **Script:** [`test_getbylabel.py`](Scripts/test_getbylabel.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbylabel.png)](Screenshots/test_getbylabel.png)

---
### 🔹 get_by_placeholder()
Locating inputs by placeholder text.

📄 **Script:** [`test_getbyplaceholder.py`](Scripts/test_getbyplaceholder.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbyplaceholder.png)](Screenshots/test_getbyplaceholder.png)

---
### 🔹 get_by_test_id()
Locating elements using test identifiers.

📄 **Script:** [`test_getbytestid.py`](Scripts/test_getbytestid.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_testbytestid.png)](Screenshots/test_testbytestid.png)

---
### 🔹 get_by_alt_text()
Locating images and elements using alternative text.

📄 **Script:** [`test_getbyalttext.py`](Scripts/test_getbyalttext.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbyalttext.png)](Screenshots/test_getbyalttext.png)

---
### 🔹 get_by_title()
Locating elements using title attributes.

📄 **Script:** [`test_getbytitle.py`](Scripts/test_getbytitle.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_getbytitle.png)](Screenshots/test_getbytitle.png)

---
### 🔹 CSS Selectors
CSS-based element selection.

📄 **Script:** [`test_cssSelector.py`](Scripts/test_cssSelector.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_cssSelector.png)](Screenshots/test_cssSelector.png)

---
### 🔹 XPath
XPath-based element selection for complex locator requirements.

📄 **Script:** [`test_xpath.py`](Scripts/test_xpath.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_xpath.png)](Screenshots/test_xpath.png)

---
### 🔹 Assertions
Playwright expect() validations for visible, enabled, title, URL and heading state.

📄 **Script:** [`test_LocatorAssertions.py`](Scripts/test_LocatorAssertions.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_LocatorAssertions.png)](Screenshots/test_LocatorAssertions.png)

---
### 🔹 Shadow DOM
Locating elements inside Shadow DOM.

📄 **Script:** [`test_locateinShadowDOM.py`](Scripts/test_locateinShadowDOM.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_locateinShadowDOM.png)](Screenshots/test_locateinShadowDOM.png)

---

### 🧬 Generator Example
An additional Playwright example included in this learning section.

📄 **Script:** [`test_generator.py`](Scripts/test_generator.py)

#### 📸 Output
[![Execution Evidence](Screenshots/test_generator.png)](Screenshots/test_generator.png)

---

## 🖼️ Existing Project Evidence

[![Project Evidence](Screenshots/project evidence.png)](Screenshots/project evidence.png)


---

## 🔑 Key Takeaway

This section demonstrates practical Playwright element identification and validation using semantic locators, CSS, XPath, Shadow DOM interaction and `expect()` assertions.
