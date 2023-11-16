from lib.grammar_stats import *
import math

# Given a string
# Check if string present has capital letter and full stop

def test_string_present_has_no_capital_and_full_stop():
    grammar = GrammarStats()
    actual = grammar.check("this is a string")
    expected = False
    assert actual == expected

def test_string_present_has_capital_and_full_stop():
    grammar = GrammarStats()
    actual = grammar.check("This is a string.")
    expected = True
    assert actual == expected

def test_if_percentage_good_returns_100_when_checked_once():
    grammar = GrammarStats()
    grammar.check("This is a string.")
    assert grammar.percentage_good() == 100


def test_if_percentage_good_returns_67_when_checked_three_times():
    grammar = GrammarStats()
    grammar.check("This is a string.")
    assert grammar.percentage_good() == 100
    grammar.check("this is a string")
    assert grammar.percentage_good() == 50
    grammar.check("this is a string")
    assert grammar.percentage_good() == 67