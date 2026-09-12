import re
import time

from playwright.sync_api import Page, expect, Playwright


def test_BrowserContext(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    context.close()
    browser.close()