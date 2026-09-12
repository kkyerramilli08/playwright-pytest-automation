import time

from playwright.sync_api import Page, expect

def test_hardassertions(page: Page) -> None:
    page.goto("https://www.saucedemo.com")
    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#user-name")).to_be_enabled()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#password")).to_be_enabled()
    expect(page.locator("#login-button")).to_be_visible()
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)


