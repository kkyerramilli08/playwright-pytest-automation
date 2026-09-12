import re
import time

from click import option
from playwright.sync_api import Page, expect

def test_HandleDropDown(page: Page):
    page.goto("https://www.salesforce.com/form/developer-signup/?d=pb")
    dropdownOptions = page.get_by_role("combobox", name="country/region").get_by_role("option").all_text_contents()
    print("Total dropdown options are :", len(dropdownOptions))
    for option in dropdownOptions:
        print(option)
