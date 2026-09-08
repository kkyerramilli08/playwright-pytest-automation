import time

from playwright.sync_api import Page
def test_get_by_text(page: Page):
    page.goto("https://jquery.com/")
    page.get_by_title("jQuery").first.click()
    time.sleep(5)
