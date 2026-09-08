import pytest

def get_data():
    return [("admin","admin123"),("user1","user123"),("user2","user123")]

@pytest.mark.parametrize("username,password",get_data())

def test_loginflow(username, password):
    print(username,"----",password)

def test_logout():
    print("Logout test")
