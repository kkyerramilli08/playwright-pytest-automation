import re
import time

from playwright.sync_api import Page, expect, Playwright


def test_CaptureVideos(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/videos/",
        record_video_size={"width": 640, "height": 480}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    context.close()
    browser.close()
