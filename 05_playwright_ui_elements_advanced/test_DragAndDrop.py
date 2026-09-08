import re
import time

from playwright.sync_api import Page, expect

def test_DragAndDrop(page: Page):
    page.goto("https://jqueryui.com/droppable/")
    frame1 = page.frame_locator(".demo-frame")

    frame1.locator("#draggable").hover()
    page.mouse.down()
    frame1.locator("#droppable").hover()
    page.mouse.up()

    time.sleep(3)
