from playwright.sync_api import Page

from LoginPage import LoginPage
from HomePage import HomePage
from CartPage import CartPage
from InfoPage import InfoPage
from OverviewPage import OverviewPage


def test_E2EScenario1(page: Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login_to_application(username="standard_user", password="secret_sauce")


    home_page = HomePage(page)
    home_page.add_first_product_to_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    info_page = InfoPage(page)
    info_page.enter_user_information(first_name="kamal", last_name="kiran", postal_code="560100")

    overview_page = OverviewPage(page)
    overview_page.placeOrder()

    page.wait_for_timeout(4000)
    home_page.logout_from_application()


