from playwright.sync_api import Page
import time


def test_ChildFrames(page: Page):
    # Step 1: Navigate to the page
    page.goto("https://ui.vision/demo/webtest/frames/")
    page.wait_for_load_state("networkidle")

    # Step 2: Get Frame 3 (frame_3.html)
    frame = page.frames[3]

    # Step 3: Fill text "john" in the input field
    frame.fill("input[name='mytext3']", "john")
    print("✓ Text filled")

    # Step 4: Click the button in the child frame
    frame.child_frames[0].click("xpath=//*[@id='i6']/div[3]/div")
    print("✓ Button clicked")

    # Step 5: Wait 2 seconds to see the result
    time.sleep(2)