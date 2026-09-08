import time

from playwright.sync_api import Page

def test_handleShadowElement(page: Page):
    page.goto("https://developer.salesforce.com/")
    page.get_by_text("Try for free").last.click()
    time.sleep(5)
    
