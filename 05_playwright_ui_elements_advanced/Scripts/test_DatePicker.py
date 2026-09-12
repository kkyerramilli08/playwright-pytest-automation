import re
import time

from playwright.sync_api import Page, expect

def test_DatePicker(page: Page):
    page.goto("https://jqueryui.com/datepicker/")
    frame1 = page.frame_locator(".demo-frame")

    frame1.locator(".hasDatepicker").click()
    frame1.locator("(//td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']//following::td)[1]").click()

    time.sleep(3)
