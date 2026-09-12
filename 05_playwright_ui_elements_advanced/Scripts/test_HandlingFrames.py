import re
import time

from playwright.sync_api import Page, expect

def test_HandlingFrames(page: Page):
    page.goto("https://jqueryui.com/tooltip/")
    frame1 = page.frame_locator(".demo-frame")
    frame1.locator("#age").fill('25')

    time.sleep(3)
