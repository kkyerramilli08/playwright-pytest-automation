import re
import time
from pathlib import Path

from playwright.sync_api import Page, expect

def test_CaptureScreenshots(page: Page):
    page.goto("https://www.amazon.com/")
    page.wait_for_timeout(5000)
    #always the same screenshot is overriding
    #instead of doing this , if we can add some date time stamp to name of screenshot
    #always screenshot will be captured dynamically as per the time of execution
    output_dir = Path(__file__).resolve().parent.parent / "Screenshots"
    output_dir.mkdir(exist_ok=True)
    page.screenshot(path=str(output_dir / f"amazon_homepage_{int(time.time())}.png"))
