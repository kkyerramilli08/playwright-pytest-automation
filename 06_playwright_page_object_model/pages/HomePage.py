from playwright.sync_api import Page

class HomePage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_container")
        self.menu_button = page.get_by_role("button", name="Menu")
        self.logout_link = page.get_by_role("link", name="Logout")

    def add_first_product_to_cart(self):
        self.add_to_cart_button.first.click()
        self.shopping_cart_icon.click()

    def logout_from_application(self):
        self.menu_button.click()
        self.logout_link.click()
