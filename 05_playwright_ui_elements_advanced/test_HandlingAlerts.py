import re
import time

from playwright.sync_api import Page, expect

def test_HandlingAlerts(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_dialog(dialog):
        dialog.accept()
    # page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", handle_dialog)
    page.get_by_text("Click for JS Alert").click()
    time.sleep(4)