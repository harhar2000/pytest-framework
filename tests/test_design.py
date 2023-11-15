from lib.design import count_words


def test_words_in_string():
    test_string = "How many words are in this string"
    result = count_words(test_string)
    assert result == 7