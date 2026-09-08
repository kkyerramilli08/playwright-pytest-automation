'''
as a part of this class LoginPage construction - I  will define all the page locators
whenever we create any object to this class LoginPage , automatically constructor will be called and
hence all the locators will be initialized and we can use them in our test cases.

as we are defining the page specific locators hence in the constructor we need to pass the page reference
'''


from playwright.sync_api import Page

class LoginPage:
        def __init__(self, page: Page):
                self.page = page
                self.username_textField = page.get_by_placeholder("Username")
                self.password_textField = page.get_by_placeholder("Password")
                self.login_button = page.get_by_role("button", name="Login")

        def login_to_application(self, username, password):
                self.username_textField.fill(username)
                self.password_textField.fill(password)
                self.login_button.click()
                  
