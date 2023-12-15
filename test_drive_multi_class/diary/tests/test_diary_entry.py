from lib.diary_entry import *

"""
Given a title and contents of diary entry
Returns title and contents of diary entry
"""

def test_diary_entry_title_and_contents():
    entry = DiaryEntry("Title", "Contents of diary on this date")
    assert entry.title == "Title"
    assert entry.contents == "Contents of diary on this date"
    

"""
When given an entry of 6 words in contents
Returns number of words in integer
"""

def test_diary_entry_word_count():
    entry = DiaryEntry("Title", "Contents of diary on this date")
    assert entry.count_words() == 6

'''
Given wpm
Returns estimate reading time it takes to read contents of a diary entry
'''

def test_reading_time():
    entry = DiaryEntry("Title", "Contents of diary on this date")
    assert entry.reading_time(2) == 3

'''
Given wpm and number of minutes available to read
Returns a chunk of contents in a diary entry the user can read
'''

def test_reading_chunk_first_time_pass():
    entry = DiaryEntry("Title", "Contents of diary on this date")
    assert entry.reading_chunk(2, 1) == "Contents of"

'''
When called again with wpm and minutes
Returns the next chunk of contents in a diary entry the user can read
'''

def test_reading_chunk_of_2wpm_1minute_called_twice():
    entry = DiaryEntry("Title", "Contents of diary on this date")
    assert entry.reading_chunk(2, 1) == "Contents of"
    assert entry.reading_chunk(2, 1) == "diary on"