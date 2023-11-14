from lib.count_words import *

def test_count_words_returns_length_of_string():
    result = count_words('I like big cats and I cannot lie')
    assert result == 8