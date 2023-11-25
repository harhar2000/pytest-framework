from lib.diary import Diary
from lib.diary_entry import DiaryEntry 
from lib.phone_number_extractor import PhoneNumberExtractor
"""
When I add multiple tasks
and I call PhoneNumberExtractor #extract
i get a list of phone numbers from all diary entries
"""
def test_extracts_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000001")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry("My Title 3", "My friend is 07800000002")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000", "07800000001", "07800000002"}


"""
When I add multiple tasks
and I call PhoneNumberExtractor #extract
It ignores dublicate numbers 
"""
def test_ignores_duplicate_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 0780000000 and 0780000001")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry("My Title 3", "My friend is 0780000000")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"0780000000", "0780000001"}






"""
When I add a diary entry
and I call PhoneNumberExtractor #extract
It ignores non-valid phone numbers
"""
def test_with_no_entries_returns_empty_list():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend's number is 07800, another number is 13141")
    diary.add(entry_1)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()



"""
When I add no diary entries   
And i call PhoneNumberExtractor #extract
It returns empty list
"""
def test_with_no_entries_returns_empty_list():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()
