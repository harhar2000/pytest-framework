from lib.StringBuilder import StringBuilder

def test_add():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello")
    stringbuilder.add(", World!")
    assert stringbuilder.output() == "Hello, World!"
    

def test_size():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello")
    assert stringbuilder.size() == 5
    stringbuilder.add(", World!")
    assert stringbuilder.size() == 13

def test_output():
    stringbuilder = StringBuilder()
    stringbuilder.add("Test")
    assert stringbuilder.output() == "Test"