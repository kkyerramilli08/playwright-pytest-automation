import re
import time

from playwright.sync_api import Page, expect

def test_Tooltip(page: Page):
    page.goto("https://jqueryui.com/tooltip/")
    frame1 = page.frame_locator(".demo-frame")
    frame1 = page.frame(url="https://jqueryui.com/resources/demos/tooltip/default.html")
    tooltipMessage = frame1.locator("#age").get_attribute("title")
    print(tooltipMessage)

    time.sleep(3)