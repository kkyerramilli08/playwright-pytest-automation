import time
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    assert page.get_by_role("link", name="Log out").is_visible() or "Logged In" in page.content()
    time.sleep(5)
    
