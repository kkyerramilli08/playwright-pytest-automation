import time
import re
from pathlib import Path

from playwright.sync_api import Page, expect

def test_UploadFiles(page: Page):
    page.goto("https://www.file.io/")
    time.sleep(1)
    base = Path(__file__).resolve().parent
    file1 = str(base / "data1.txt")
    file2 = str(base / "data2.txt")
    page.locator("//label[@for='select-files-input']").set_input_files([file1, file2])

    time.sleep(5)
