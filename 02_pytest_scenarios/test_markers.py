import pytest

@pytest.mark.sanity
def test_login():
    print("Login flow")

@pytest.mark.smoke
def test_logout():
    print("Logout flow")

@pytest.mark.reg
def test_create():
    print("Create flow")



# def test_login():
#     print("Login flow")
#
# def test_logout():
#     print("Logout flow")
#
# def test_create():
#     print("Create flow")

