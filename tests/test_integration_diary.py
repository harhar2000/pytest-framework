from lib.diary import Diary
from lib.c5_diaryEntry import DiaryEntry
"""

### Describe Problem - 
    Diary let's me add entries which append into a list.
    Count the number of words in all diary entries
    Integer estimate of total reading time in minutes of total diary
    Return the page with the word count that best matches the reading speed



### Design Class Interface - Include initialise, public properties and public methods with all parameters, return values and side effects

### Create Examples as Tests - List of exmaples how class will behave in different situations via tests


### Implement Behaviour - After each test adjust code




Given I adds two diary entries
I see them back in the list
"""

def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]



"""
Given I add two diary entries
and I call #count_words
I get the sum of all words in the contents of diary entries
"""
def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two")
    entry_2 = DiaryEntry("My Title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
Given I add two diary entries with a total length of 5
And I call #reading_time with a wpm of 2
Then the total reading time hsould be 3
"""
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two")
    entry_2 = DiaryEntry("My Title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
Given I add two diary entries, one long and one short
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I cna only read the short one
Then #find_best_entry_for_reading_time returns the shorter one 
"""
def test_find_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two three")
    entry_2 = DiaryEntry("My Title 2", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1




"""
Given I add a diary entry 
And I call #find_best_entry_for_reading_time
wiht a wpm and minutes that means I cannot read that entry
Then #find_best_entry_for_reading_time returns None
"""
def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None


"""
Given I add two diary entries
And I call #find_best_entry_for_reading_time
With a wpm and minutes that emans I could read both
Then #find_best_entry_for_reading_time returns the longer one
"""
def test_find_best_entry_for_reading_time_returns_the_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two three")
    entry_2 = DiaryEntry("My Title 2", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2