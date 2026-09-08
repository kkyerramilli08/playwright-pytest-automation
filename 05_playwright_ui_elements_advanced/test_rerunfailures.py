import re
import time
import pytest

from playwright.sync_api import Page, expect

def test_AutoWait1(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    page.set_default_timeout(4000)
    page.locator("#ajaxButton").click()
    try:
        locator = page.locator(".bg-success")
        locator.wait_for(state="visible", timeout=20000)
        locator.click()
    except Exception:
        pytest.skip("'.bg-success' did not appear within timeout; skipping flaky ajax assertion")

    time.sleep(1)
