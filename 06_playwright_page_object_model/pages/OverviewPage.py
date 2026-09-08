from playwright.sync_api import Page

class OverviewPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.get_by_role("button", name="Finish")
        self.back_home_button = page.get_by_role("button", name="Back Home")

    def placeOrder(self):
        self.finish_button.click()
        self.back_home_button.click()
