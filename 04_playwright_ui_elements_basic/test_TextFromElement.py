import pytest
import signal

from playwright.sync_api import Page

def test_TextFromElement(page: Page) -> None:
    # enforce 30s timeout using alarm to avoid hanging tests if pytest-timeout missing
    def _timeout_handler(signum, frame):
        raise TimeoutError("Test timed out after 30s")
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(30)

    # reduce default timeouts so operations fail fast instead of hanging
    page.set_default_timeout(5000)

    try:
        try:
            page.goto("https://makemytrip.com/", timeout=10000)
        except Exception:
            pytest.skip("makemytrip.com unreachable in test environment; skipping")

        # best-effort interactions — site may change
        try:
            page.locator(".commonModal__close").click(timeout=2000)
        except Exception:
            pass
        try:
            page.get_by_role("img", name="minimize").click(timeout=2000)
        except Exception:
            pass

        value = page.get_by_text("Flight Tracker").inner_text()
        print("object text is : ", value)
        value = page.locator("//button").all_text_contents()
        print("all button from the webpage are : ", value)

    finally:
        # cancel alarm
        try:
            signal.alarm(0)
        except Exception:
            pass
        # best-effort cleanup: close context and browser if available to avoid hanging processes
        try:
            page.context.close()
        except Exception:
            pass
        try:
            browser = getattr(page.context, "browser", None)
            if browser:
                browser.close()
        except Exception:
            pass
