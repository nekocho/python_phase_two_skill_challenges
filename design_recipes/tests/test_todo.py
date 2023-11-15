import pytest
from lib.todo import *

def test_no_todo_returns_false():
    expected = check_todo("I am not a to do list")
    actual = False
    assert actual == expected

def test_todo_present_returns_true():
    expected = check_todo("#TODO Groceries, Chores, Cleaning")
    actual = True
    assert actual == expected

def test_throw_error_if_no_text():
    with pytest.raises(Exception) as e:
        check_todo("")
    error_message = str(e.value)
    assert error_message == "No text found!"