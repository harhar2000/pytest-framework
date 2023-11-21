from lib.diary_entry import DiaryEntry
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

"""
When I initialise with a five-word contents
then #reading_time with a wpm of 2 should return 3
"""

def test_reading_time():
    diary_entry = DiaryEntry("My Title", "one two thee four five")
    assert diary_entry.reading_time(2) == 3

"""
When I initialise with a five-word contents
Then, at first, #reading_chunk should return the first chunk
readable in the time
"""

def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My Title", "one two three our five")
    assert diary_entry.reading_chunk(2, 1) == 'one two'