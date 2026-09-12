import time

from playwright.sync_api import Page
#id="SearchBox" , #id-> CSS selector for that element
#class="classname", .classname-> for that element
#placeholder = "enter name", [placeholder='value']
#.classname [attribute='value']

def test_css_selector(page: Page):
    page.goto("https://saucedemo.com/")

    # if an element is having an ID how to convert in to cssSelector.
    # as per syntax we just need to use '#' , inspect the element
    # this id is having an id = "user-name" , an attribute associated value
    # copy the associated value "user-name" and paste it after #
    # so the cssSelector will be #user-name
    page.locator("#user-name").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator(".submit-button").click()
    #page.locator("#login-button").click()
    time.sleep(10)





