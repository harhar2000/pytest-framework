from lib.diary import Diary
 # initially diary has no entries

def test_diary_is_initially_empty():
    diary = Diary()
    assert diary.all() == []
    
