import time
import pytest

from playwright.sync_api import Page
def test_get_by_text(page: Page):
    page.goto("https://www.salesforce.com/products/free-trial/developer/")
    locator = page.get_by_text("Sign me up")
    if locator.count() == 0:
        pytest.skip("'Sign me up' not found on salesforce page; skipping")
    locator.click()
    time.sleep(1)

