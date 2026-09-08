import pytest

# Configure pytest-asyncio to not interfere with sync tests
pytest_plugins = ('pytest_asyncio',)

# This tells pytest-asyncio to only handle tests explicitly marked as async
# Do NOT auto-apply the asyncio mode to all tests
def pytest_collection_modifyitems(items):
    """
    This function modifies test collection to ensure:
    - Async tests (async def) work with asyncio
    - Sync tests (def) work normally
    """
    for item in items:
        # Check if the test function is a coroutine (async def)
        if hasattr(item, 'function'):
            import inspect
            if inspect.iscoroutinefunction(item.function):
                # Mark async tests with asyncio marker
                item.add_marker(pytest.mark.asyncio)

# Dismiss common cookie/consent overlays that may block interactions
@pytest.fixture(autouse=True)
def dismiss_cookie_banner(page, pytestconfig):
    """Autouse fixture that removes overlays blocking pointer events.

    Also wraps page.goto to:
    - use domcontentloaded by default
    - honor a project-level base-url when tests call page.goto with a leading '/'

    To set base URL, add in pytest.ini:
        [pytest]
        base_url = https://example.com
    or pass on the CLI: pytest --base-url=https://example.com
    """
    import os
    from urllib.parse import urljoin

    script = '''() => {
        // Remove common overlays
        const selectors = ['#onetrust-consent-sdk', '.onetrust-pc-dark-filter', '[id^="onetrust"]', '.qc-cmp2-container', '.cookie-consent', '[role="dialog"]', '.modal-overlay'];
        selectors.forEach(s => {
            document.querySelectorAll(s).forEach(el => el.remove());
        });
        // Remove pointer-events blocking from html and body
        document.documentElement.style.pointerEvents = 'auto';
        document.body.style.pointerEvents = 'auto';
    }'''
    
    # Set default navigation timeout to 90 seconds
    page.set_default_timeout(90000)
    page.set_default_navigation_timeout(90000)
    
    original_goto = page.goto
    def goto_and_cleanup(url, *args, **kwargs):
        # resolve relative URLs against configured base_url (if provided)
        try:
            if isinstance(url, str) and url.startswith('/'):
                base = None
                # CLI option registered by plugins or user may be 'base_url' or 'base-url'
                try:
                    base = pytestconfig.getoption('base_url')
                except Exception:
                    try:
                        base = pytestconfig.getoption('base-url')
                    except Exception:
                        base = None
                # allow environment variable fallback
                if not base:
                    base = os.environ.get('BASE_URL') or os.environ.get('PLAYWRIGHT_BASE_URL')
                if base:
                    url = urljoin(base.rstrip('/')+'/', url.lstrip('/'))
                else:
                    raise ValueError("Relative URL passed to page.goto but no base_url configured. Set base_url in pytest.ini or pass --base-url on CLI or set BASE_URL env var.")
        except Exception as e:
            # surface helpful error instead of Playwright's 'invalid URL' protocol error
            raise

        # Use domcontentloaded for faster navigation (doesn't wait for all resources)
        if 'wait_until' not in kwargs:
            kwargs['wait_until'] = 'domcontentloaded'
        # Set timeout to 90 seconds if not specified
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 90000
        
        res = original_goto(url, *args, **kwargs)
        try:
            page.evaluate(script)
        except Exception:
            pass
        return res
    page.goto = goto_and_cleanup
    
    try:
        page.evaluate(script)
    except Exception:
        pass
