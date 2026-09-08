import re
import time

from playwright.sync_api import Page, expect

def test_WebTable1(page: Page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")

    # To get fifth row Island Trading value to be printed.
    value1 = page.locator("//tr[5]/td[1]").first.inner_text()
    print(value1)

    time.sleep(3)
