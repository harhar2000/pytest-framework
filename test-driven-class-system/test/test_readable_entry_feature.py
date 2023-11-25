from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.readable_entry_extractor import ReadableEntryExtractor

"""
When I add one diary entry that fits in the time
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It gets that diary entry
"""

def test_gets_single_entry_that_fits_in_th_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three four")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_1


"""
When I add one diary entry that does not fit in the time
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns None
"""
def test_returns_none_if_entries_do_not_fit_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three four five")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    extractor.extract(wpm=2, minutes=2) == None




"""
When I add multiple diary entries, one readable 
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns the readable one
"""
def test_gets_readable_out_of_readable_and_unreadable():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three four five")
    entry_2 = DiaryEntry("Title", "one two three four")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_2



"""
When I add multiple diary entries, multiple readable 
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns the longest readable one
"""
def test_gets_Longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three four")
    entry_2 = DiaryEntry("Title", "one two three")
    entry_3 = DiaryEntry("Title", "one two three four five six seven")
    entry_4 = DiaryEntry("Title", "one two three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=3) == entry_4




"""
When I add no diary entries   
And i call ReadableEntryExtractor #extract
It returns None
"""
def test_with_no_entries_returns_none():
    diary = Diary()
    extractor = ReadableEntryExtractor(diary)
    extractor.extract(wpm=2, minutes=2) # => entry_2
