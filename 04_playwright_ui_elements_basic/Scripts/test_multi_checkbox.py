import re
import time

from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.bing.com/account/general?ru")
    checkboxes = page.get_by_role("checkbox")

    count = checkboxes.count()
    print("Total number of checkboxes are :", count)

    for i in range(4):
        checkboxes.nth(i).uncheck()
        time.sleep(2)
