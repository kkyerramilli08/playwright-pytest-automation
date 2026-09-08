import re
import time

from playwright.sync_api import Page, expect

def test_MouseHover(page: Page):
    page.goto("https://www.emirates.com/in/english/book/?utm_source=")
    page.get_by_text("About booking online").first.hover()

    time.sleep(3)
