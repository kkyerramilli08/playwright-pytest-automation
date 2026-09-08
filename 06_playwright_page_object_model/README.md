# Page Object Model (POM) – Playwright + Pytest

Page Object Model (POM) design pattern implemented within the Python + Playwright + Pytest automation project.

## Structure

- **pages/** - Page classes containing reusable locators and page actions.
- **test_E2EScenario1.py** - End-to-end test scenario using the page classes.
- **Random_Data.py** - Test data used by the automation scenario.
- **test_runner.py** - Test execution entry point.

## Page Objects

- LoginPage
- HomePage
- InfoPage
- OverviewPage
- CartPage

## Implementation

The page classes separate web-page interaction logic from test logic, allowing reusable locators and actions to be used across the E2E scenario.

The POM implementation is part of the overall Python + Playwright + Pytest automation project.
