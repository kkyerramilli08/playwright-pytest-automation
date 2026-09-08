import pytest

@pytest.fixture(scope='module')
def setup():
    print("DB connection established")

    yield
    print("DB connection closed")

@pytest.fixture(scope='function')
def before_each_function():
    print("establishing connection with IOS Driver")

    yield
    print("closing connection with IOS Driver")

@pytest.mark.usefixtures('setup', 'before_each_function')
def test_logout():
    print("logout test")



