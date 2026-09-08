import time

from playwright.sync_api import Page, expect

def test_Suggestions(page: Page):
    page.goto("https://www.bing.com/")
    page.locator("#sb_form_q").fill("playwright")
    # page.get_by_role("combobox").fill("playwright")
    page.get_by_role("combobox").click()
    time.sleep(5)
    suggestionsText: list[str] = page.locator(".sa_sg  .sa_mlti_line").all_inner_texts()
    rowcount = len(suggestionsText)
    print("total  number of suggestions are :",rowcount)
    for suggestion in suggestionsText:
        print(suggestion)

        time.sleep(1)

