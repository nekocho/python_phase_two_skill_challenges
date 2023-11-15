import pytest
from lib.grammar_check import *

def test_string_of_text_is_text():
    expected = grammar_check("Hi my name is fiona.")
    actual = "Hi my name is fiona."
    assert actual == expected

def test_capitalised_first_letter_in_string():
    expected = grammar_check("today's weather is sunny.")
    actual = "Today's weather is sunny."
    assert actual == expected

def test_capitalised_first_letter_and_full_stop_at_end_of_string():
    expected = grammar_check("today has been quite cold")
    actual = "Today has been quite cold."
    assert actual == expected

def test_if_no_string_throws_error():
    with pytest.raises(Exception) as e:
        grammar_check("")
    error_message = str(e.value)
    assert error_message == "No text provided!"
