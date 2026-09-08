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
def dismiss_cookie_banner(page):
    """Autouse fixture that removes overlays blocking pointer events."""
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
