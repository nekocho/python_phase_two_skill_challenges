from lib.diary import *


"""
If no diary entry
returns empty list
"""

def test_no_diary_entry():
    diary = Diary()
    assert diary.all() == []