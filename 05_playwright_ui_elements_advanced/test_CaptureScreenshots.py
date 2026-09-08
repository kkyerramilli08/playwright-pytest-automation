import re
import time

from playwright.sync_api import Page, expect

def test_CaptureScreenshots(page: Page):
    page.goto("https://www.amazon.com/")
    page.wait_for_timeout(5000)
    # page.screenshot(path="/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/screenshots/amazon_homepage.png")
    #always the same screenshot is overriding
    #instead of doing this , if we can add some date time stamp to name of screenshot
    #always screenshot will be captured dynamically as per the time of execution
    page.screenshot(path=f"/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/screenshots/amazon_homepage_{int(time.time())}.png")
    # page.screenshot(path=f"/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/screenshots/amazon_homepage_{int(time.time())}.png", full_page=True)
    # page.locator("#nav-search-submit-button").screenshot(path=f"/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/screenshots/amazon_homepage_{int(time.time())}.png")
