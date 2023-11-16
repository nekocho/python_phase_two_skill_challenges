from lib.diaryentry import *

def test_if_title_and_contents_is_string():
    diary = DiaryEntry("test", "contents test")
    assert diary.title == "test"
    assert diary.contents == "contents test"

def test_format():
    diary = DiaryEntry("test", "contents test")
    assert diary.format() == "test: contents test"

def test_count_words():
    diary = DiaryEntry("test", "contents test")
    assert diary.count_words() == 2

def test_reading_time():
    diary = DiaryEntry("test", "contents test")
    assert diary.reading_time(2) == 1

def test_reading_chunk():
    diary = DiaryEntry("test", "contents test")
    assert diary.reading_chunk(1, 1) == ["contents"]

def test_reading_chunk_for_2wpm_3minutes():
    diary = diary = DiaryEntry("Title", "This is a longer diary entry")
    assert diary.reading_chunk(2, 3) == ["This is", "a longer", "diary entry"]