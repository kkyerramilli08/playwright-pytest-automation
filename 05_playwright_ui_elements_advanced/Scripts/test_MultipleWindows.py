import re
import time

from playwright.sync_api import Page, expect, Playwright

def test_MultipleWindows(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://homeloans.hdfc.bank.in/")
    page.wait_for_timeout(3000)
    page.get_by_text("Blogs").first.click()
    page.wait_for_timeout(3000)
    allPages=context.pages
    print("Total number of pages:",len(allPages))
    childPage=allPages[1] # as my required page is 2nd page
    childPage.wait_for_load_state()
    print("Child page title is:",childPage.title())
    print("Child page URL is:",childPage.url)
    childPage.locator("#close-disclaimer").click()

    time.sleep(3)
