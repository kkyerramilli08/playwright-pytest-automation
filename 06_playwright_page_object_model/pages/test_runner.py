from playwright.sync_api import Page

from Random_Data import Random_Data

def test_runner(page: Page):
    page.goto("https://www.saucedemo.com/")
    random_data = Random_Data()
    fname: str = random_data.get_first_name()
    page.get_by_placeholder("Username").fill(fname)

