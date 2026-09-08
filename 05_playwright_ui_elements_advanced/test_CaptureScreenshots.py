import re
import time

from playwright.sync_api import Page, expect

def test_CaptureScreenshots(page: Page):
    page.goto("https://www.amazon.com/")
    page.wait_for_timeout(5000)

    # Save screenshots in a repo-local Reports/screenshots directory so tests are portable
    from pathlib import Path
    out_dir = Path(__file__).resolve().parent / "Reports" / "screenshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = out_dir / f"amazon_homepage_{int(time.time())}.png"

    page.screenshot(path=str(filename))
    # full page example:
    # page.screenshot(path=str(out_dir / f"amazon_homepage_full_{int(time.time())}.png"), full_page=True)
