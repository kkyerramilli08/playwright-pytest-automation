from playwright.sync_api import Page

class InfoPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.postal_code_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def enter_user_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)
        self.continue_button.click()
