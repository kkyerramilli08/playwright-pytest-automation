import pytest

def setup_module(module):
    print("DB connection established")
def teardown_module(module):
    print("DB connection closed")

def test_login():
    print("Login test")

def test_logout():
    print("Logout test")

