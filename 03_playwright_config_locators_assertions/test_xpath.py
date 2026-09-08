import time

from playwright.sync_api import Page

def test_xpath(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("//*[@id='user-name']").fill("standard_user")
    page.locator("//*[@id='password']").fill("secret_sauce")
    page.locator("//input[@data-test= 'login-button']").click()
    time.sleep(5)

