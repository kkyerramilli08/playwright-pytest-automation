import re
import time

from playwright.sync_api import Page, expect

def test_EndToEndFlow(page: Page):
    page.goto("https://www.saucedemo.com/")
    #step 1: login to application
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    #step 2: add product to cart
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_container").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    #step 3: checkout
    page.get_by_role("button", name="Checkout").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    page.get_by_placeholder("First Name").fill("Kamal")
    page.get_by_placeholder("Last Name").fill("Kiran")
    page.get_by_placeholder("Zip/Postal Code").fill("560100")
    page.get_by_role("button", name="Continue").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    #step 4: finish
    page.get_by_role("button", name="Finish").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    time.sleep(3)
    #step 5: back to home button clicking
    page.get_by_role("button", name="Back Home").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    time.sleep(3)
    #step 6: logout from application
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://www.saucedemo.com/")
    time.sleep(3)


