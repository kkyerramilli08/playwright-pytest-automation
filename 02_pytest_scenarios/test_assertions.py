from builtins import input

import pytest

def test_assertions():
    input = "kamal kiran"
    output = "kamal kiran"
    inputdata = "kamal kiran"

    print("code started")
    assert input == output, "both strings not matched, Test failed"
    assert "kamal kiran" in inputdata, "data not found"
    # assert False , "default failed"
    print("code ended")



# def test_assertions():
#     input = "kamal kiran"
#     output ="kamal k"
#     if input == output:
#         print("both are equal & Test passed")
#     else:
#         print("Test failed")
