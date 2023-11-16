from lib.make_snippet import *

def test_make_snippet_returns_string_less_than_5():
    result = make_snippet('Hi, I am a string')
    assert result == 'Hi, I am a string'

def test_make_snippet_returns_sliced_string_over_5():
    result = make_snippet('Hi, I am a longer string')
    assert result == 'Hi, I am a longer...'   