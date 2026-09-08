import pytest

@pytest.mark.order(1)
def test_loginApp():
    print("this is login app test")

@pytest.mark.order(5)
def test_logoutApp():
    print("this is logout app test")

@pytest.mark.order(2)
def test_searchApp():
    print("this is search app test")

@pytest.mark.order(3)
def test_createUser():
    print("this is create user test")

@pytest.mark.order(6)
def test_editUser():
    print("this is edit user test")

@pytest.mark.order(4)
def test_deleteUser():
    print("this is delete user test")


