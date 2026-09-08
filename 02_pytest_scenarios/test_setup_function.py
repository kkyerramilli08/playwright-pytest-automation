import time

import pytest

def setup_function(function):
    print("Appium server start")
def teardown_function(function):
    print("Appium server stop")

def test_login():
    print("Login test")

def test_logout():
    print("Logout test")

    time.sleep(5)

