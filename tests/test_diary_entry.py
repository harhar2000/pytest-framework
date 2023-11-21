from lib.diaryEntry import DiaryEntry
"""
When I initialise with title and contents
I can get that title and contents back
"""
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

"""
When I initialise with a five-word contents
Then #count_words should return five
"""
def test_count_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.count_words() == 5

    