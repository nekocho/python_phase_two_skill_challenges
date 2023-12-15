## Diary Multi-class

# Integration tests - Diary:


'''
When one diary entry added
When requesting diary entries
Returns list of one diary entry
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.all() => ["Titlen Contents of diary on this date"]


'''
When two diary entries added
When requesting diary entries
Returns list of two diary entries
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
diary.all() => ["Title Contents of diary on this date", "Second Title Contents of diary for the day before"]

'''
Given a single diary entry
Return integer of word count
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.count_words() => 7

'''
Given two diary entries
Return integer of total word count of both diary entries
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
diary.count_words() => 16


'''
Given wpm of 2
Returns the number of minutes it would take to read all diary entries
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
diary.reading_time(2) => 8

'''
Given wpm of 2 and 4 minutes
Returns the diary entry the user can read within this time frame (not over)
'''

diary = Diary()
diary.add(DiaryEntry("Title", "Contents of diary on this date"))
diary.add(DiaryEntry("Second Title", "Contents of diary for the day before"))
diary.find_best_entry_for_reading_time(2, 4) => "Title: Contents of diary on this date"




# Unit test - Diary entry:

'''
Given a diary entry
Returns number of words in contents
'''
diaryentry = DiaryEntry("Title", "Contents of diary on this date")
diaryentry.count_words() => 6


'''
Given wpm
Returns estimate reading time it takes to read contents of a diary entry
'''
diaryentry = DiaryEntry("Title", "Contents of diary on this date")
diaryentry.reading_time(2) => 3

'''
Given wpm and number of minutes available to read
Returns a chunk of contents in a diary entry the user can read
'''

diaryentry = DiaryEntry("Title", "Contents of diary on this date")
diaryentry.reading_chunk(2, 1) => "Contents of"

'''
When called again with wpm and minutes
Returns the next chunk of contents in a diary entry the user can read
'''

diaryentry = DiaryEntry("Title", "Contents of diary on this date")
diaryentry.reading_chunk(2, 1) => "diary on"
