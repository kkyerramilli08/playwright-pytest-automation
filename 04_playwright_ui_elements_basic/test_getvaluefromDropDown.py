from playwright.sync_api import Page, expect


def test_getvaluefromDropDown(page: Page) -> None:
    page.set_content(
        """
        <button id="menuButton" aria-expanded="false">Dropdown</button>
        <div id="menu" hidden>
            <button type="button">Action</button>
            <button type="button">Another action</button>
            <button type="button">Something else here</button>
        </div>
        <script>
            const button = document.getElementById('menuButton');
            const menu = document.getElementById('menu');
            button.addEventListener('click', () => {
                const expanded = button.getAttribute('aria-expanded') === 'true';
                button.setAttribute('aria-expanded', String(!expanded));
                menu.hidden = expanded;
            });
            menu.addEventListener('click', (event) => {
                const selected = event.target.closest('button');
                if (!selected) return;
                button.textContent = selected.textContent.trim();
                menu.hidden = true;
                button.setAttribute('aria-expanded', 'false');
            });
        </script>
        """
    )

    page.locator("#menuButton").click()
    page.get_by_text("Something else here").click()
    expect(page.locator("#menuButton")).to_have_text("Something else here")

