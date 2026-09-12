import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()



