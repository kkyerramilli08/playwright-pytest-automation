import re
import time

from playwright.sync_api import Page, expect

def test_AlertConfirm(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_dialog(dialog):
        print("Dialog message:", dialog.message)
        print("Dialog type:", dialog.type)
        assert dialog.type == "confirm"
        assert dialog.message == "I am a JS Confirm"

        dialog.dismiss()

    page.on("dialog", handle_dialog)
    page.get_by_text("Click for JS Confirm").click()
    time.sleep(2)
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

    time.sleep(3)
