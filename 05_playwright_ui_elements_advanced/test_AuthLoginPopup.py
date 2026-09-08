import re
import time

from playwright.sync_api import Page, expect, Playwright


def test_AuthLoginPopup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # isolated browser clean state context
    # context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_timeout(5000)
    # page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page.locator("#content")).to_be_visible()
    context.close()
    browser.close()