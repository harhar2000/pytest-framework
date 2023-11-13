from greet import greet

def test_greet_returns_name_string():
    result = greet("Jon")
    assert result == "Hello, Jon!"