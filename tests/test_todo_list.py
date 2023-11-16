from lib.todo_list import *

def test_empty_list_returns_empty():
    todo_list = todo_list()
    result = todo_list()
    assert result == "All tasks complete"


def test_list_of_one_returns_one():
    todo_list = todo_list()
    result = todo_list("Do shopping")
    assert result == "Do shopping"


def test_list_of_three_returns_three():
    todo_list = todo_list()
    result = todo_list("Do Shopping, Read Book, Pick up Child")
    assert result == "Do Shopping, Read Book, Pick up Child"