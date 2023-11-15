from lib.make_snippett import make_snippet

def test_string_length_5_or_less():
    test_string = "Hello world"
    result = make_snippet(test_string)
    assert len(result.split()) <= 5  

def test_string_length_6_plus():
    test_string = "This string does have six words"
    result = make_snippet(test_string)
    assert result.endswith("...")
    assert len(result.split()) == 5
