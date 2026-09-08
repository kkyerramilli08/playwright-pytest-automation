import re
import time

from playwright.sync_api import Page, expect

def test_HandleDropDown(page: Page):
    page.goto("https://testpages.herokuapp.com/pages/forms/html-form/")
    time.sleep(1)
    # page.get_by_role("listbox").select_option(["Selection Item 1", "Selection Item 3"])
    # to select all the contents in the list box, use all text contents
    # multiSelectOptions: list[str] = page.get_by_role("listbox").get_by_role("option").all_text_contents()
    # here i also user all_inner_texts() to get the inner text of all the options in the list box
    # all_inner_texts will remove all additional spaces before particular string and after the vlue aswell
    multiSelectOptions: list[str] = page.get_by_role("listbox").get_by_role("option").all_inner_texts()
    for option in multiSelectOptions:
        print(option)