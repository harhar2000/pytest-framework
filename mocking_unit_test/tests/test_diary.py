from unittest.mock import Mock
from lib.diary import Diary

def test_diary_counts_words_in_all_entries():
    diary = Diary()
    four_word_mock = Mock()
    four_word_mock.count_words.return_value = 4
    diary.add(four_word_mock)
    two_word_mock = Mock()
    two_word_mock.count_words.return_value = 2
    diary.add(two_word_mock)
    assert diary.count_words() == 6

def test_diary_entry_counts_words_in_a_single_entry():
    diary = Diary()
    four_word_mock = Mock()
    four_word_mock.count_words.return_value = 4
    diary.add(four_word_mock)
    assert diary.count_words() == 4