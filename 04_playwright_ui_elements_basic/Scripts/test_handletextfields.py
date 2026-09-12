import time

from playwright.sync_api import Page, expect

def test_handle_text_fields(page: Page) -> None:
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").clear()
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").clear()
    page.locator("//input[@placeholder='Password']").fill("secret_sauce")
    time.sleep(5)
