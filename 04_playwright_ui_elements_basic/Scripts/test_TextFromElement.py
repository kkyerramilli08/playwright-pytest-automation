import time
import pytest

from playwright.sync_api import Page, expect

def test_TextFromElement(page: Page) -> None:
    try:
        page.goto("https://makemytrip.com/")
    except Exception:
        pytest.skip("makemytrip.com unreachable in test environment; skipping")
    # best-effort interactions — site may change
    try:
        page.locator(".commonModal__close").click()
    except Exception:
        pass
    try:
        page.get_by_role("img", name="minimize").click()
    except Exception:
        pass
    value = page.get_by_text("Flight Tracker").inner_text()
    print("object text is : ", value)
    value = page.locator("//button").all_text_contents()
    print("all button from the webpage are : ", value)
    time.sleep(1)

