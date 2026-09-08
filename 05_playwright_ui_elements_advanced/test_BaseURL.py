import re
import time

from playwright.sync_api import Page, expect

def test_BaseURL(page: Page):
    page.goto("/")

    time.sleep(2)
