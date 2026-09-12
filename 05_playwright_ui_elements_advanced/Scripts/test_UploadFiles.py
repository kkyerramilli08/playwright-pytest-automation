import time
from pathlib import Path
import re

from playwright.sync_api import Page, expect

def test_UploadFiles(page: Page):
    page.goto("https://www.file.io/")
    time.sleep(1)
    file1 = str(Path(__file__).resolve().parent / "data1.txt")
    file2 = str(Path(__file__).resolve().parent / "data2.txt")
    page.locator("//label[@for='select-files-input']").set_input_files([file1, file2])

    time.sleep(5)
