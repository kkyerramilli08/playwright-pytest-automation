import re
import time

from playwright.sync_api import Page,expect

def test_getvaluefromDropDown(page: Page) -> None:

    page.goto("https://getbootstrap.com/docs/5.3/components/dropdowns/")
    page.locator("(//button[@class='btn btn-secondary dropdown-toggle'])[1]").click()
    time.sleep(1)
    page.get_by_text("Something else here").first.click()
    time.sleep(2)

