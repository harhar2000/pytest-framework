
from lib.make_snippet import make_snippet

def test_string_length_5_or_less():
    test_string = "Hello world"
    result = make_snippet(test_string)
    assert len(make_snippet) <= 5 
    # 
    # 

def test_string_length_6_plus():
    test_string = "This string does have six words"
    result = make_snippet(test_string)
    assert result.endswith("...")
    assert len(result.split()) == 6
    # Return five words + "..." if len(make_snippet) > 5
    #
    #