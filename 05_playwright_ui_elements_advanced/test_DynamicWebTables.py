import re
import time

from playwright.sync_api import Page, expect

def test_WebTable1(page: Page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    tableRows = page.locator("#customers").get_by_role("row")
    rowCount = tableRows.count()
    print("Total number of rows:", rowCount)
    for i in range(1, rowCount):
        rowValue = tableRows.nth(i).locator("//td[1]").inner_text()
        print(rowValue)

        time.sleep(3)

