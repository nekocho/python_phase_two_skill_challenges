from lib.diary_entry import *
from lib.diary import *

'''
Given an entry
Adds entry to Diary
'''

def test_add_single_diary_entry_to_diary_return_all():
    diary = Diary()
    entry1 = DiaryEntry("Title", "Contents of diary on this date")
    diary.add(entry1)
    actual = diary.all()
    
    assert actual == [entry1]

'''
Given two diary entries
Adds both to Diary
'''


def test_add_two_diary_entry_to_diary_return_all():
    diary = Diary()
    entry1 = DiaryEntry("Title", "Contents of diary on this date")
    entry2 = DiaryEntry("Second Title", "Contents of diary for the day before")
    diary.add(entry1)
    diary.add(entry2)
    actual = diary.all()
    
    assert actual == [entry1, entry2]

'''
Given a single diary entry
Return integer of word count
'''
def test_word_count_of_single_diary_entry_return_integer():
    diary = Diary()
    diary.add(DiaryEntry("Title", "Contents of diary on this date"))
    actual = diary.count_words()
    expected = 6
    assert actual == expected

'''
Given two diary entries
Return integer of total word count of both diary entries
'''
def test_word_count_of_two_diary_entry_return_integer():
    diary = Diary()
    diary.add(DiaryEntry("Title", "Contents of diary on this date"))
    diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
    actual = diary.count_words()
    expected = 13
    assert actual == expected

'''
Given wpm of 2
Returns the number of minutes it would take to read all diary entries
'''
def test_reading_time_of_2wpm_return_7minutes_reading_time():
    diary = Diary()
    diary.add(DiaryEntry("Title", "Contents of diary on this date"))
    diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
    actual = diary.reading_time(2)
    expected = 7
    assert actual == expected

'''
Given wpm of 1 and 1 minutes
Returns the diary entry the user can read within this time frame (not over)
'''
def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Title", "Contents")
    entry2 = DiaryEntry("Second Title", "Contents of diary for the day before with more words than the last")
    diary.add(entry1)
    diary.add(entry2)
    actual = diary.find_best_entry_for_reading_time(1, 1) 
    expected = entry1
    assert actual == expected

'''
Given wpm of 2 and 3 minutes
Returns the diary entry the user can read within this time frame (not over)
'''
def test_best_entry_for_reading_time_for_2wpm_and_3min():
    diary = Diary()
    entry1 = DiaryEntry("Title", "Contents of diary from yesterday but with more words now")
    entry2 = DiaryEntry("Second Title", "Contents here and here and here")
    diary.add(entry1)
    diary.add(entry2)
    actual = diary.find_best_entry_for_reading_time(2,3) 
    expected = entry2
    assert actual == expected