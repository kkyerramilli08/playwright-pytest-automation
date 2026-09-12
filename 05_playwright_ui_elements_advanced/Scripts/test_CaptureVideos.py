import re
import time
from pathlib import Path

from playwright.sync_api import Page, expect, Playwright


def test_CaptureVideos(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir=str(Path(__file__).resolve().parent.parent / "Videos"),
        record_video_size={"width": 640, "height": 480}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    context.close()
    browser.close()
