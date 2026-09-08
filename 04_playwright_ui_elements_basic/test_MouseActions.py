import re
import time

from playwright.sync_api import Page, expect

def test_MouseActions(page: Page):
    page.goto("https://www.saucedemo.com/")
    # page.locator("#login-button").dblclick()

    #perform right click on login button
    # page.locator("#login-button").click(button="right")

    # click on top left corner of login button
    # page.locator("#login-button").click(position={"x": 0, "y": 0})

    #press keys sequentially with mouse
    # page.locator("#user-name").click()
    # page.locator("#user-name").press_sequentially("standard_user")

    # press keys sequentially with delay
    page.locator("#user-name").click()
    page.locator("#user-name").press_sequentially("standard_user", delay=500)

    time.sleep(3)
