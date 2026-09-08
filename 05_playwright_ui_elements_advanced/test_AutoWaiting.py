import re
import time

from playwright.sync_api import Page, expect

def test_AutoWait(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    # page.set_default_timeout(4000)
    page.locator("#ajaxButton").click()
    # page.wait_for_timeout(20000) #strictly wait for 20 seconds to see the effect
    confirmationMessage = page.locator(".bg-success").inner_text()
    print(confirmationMessage)


    time.sleep(3)
