from lib.diary_entry import DiaryEntry

def test_diary_entry_constructs():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title # => "My Title"
    assert entry.contents # => "My Contents
