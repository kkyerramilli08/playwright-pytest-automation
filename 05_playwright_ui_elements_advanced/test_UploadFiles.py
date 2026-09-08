import time
import re

from playwright.sync_api import Page, expect

def test_UploadFiles(page: Page):
    page.goto("https://www.file.io/")
    time.sleep(1)
    file1 = "/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/data1.txt"
    file2 = "/media/jaanu/F1 RACE/QA engineer/pycharmproject/03_playwright_pytest/Interacting with UI Elements/02_Advanced/data2.txt"
    page.locator("//label[@for='select-files-input']").set_input_files([file1, file2])

    time.sleep(5)
