import time

from playwright.sync_api import Page
def test_get_by_text(page: Page):
    page.goto("https://www.emirates.com/in/english/book/")
    page.get_by_test_id("combobox_Departure airport").click()
    time.sleep(10)
    