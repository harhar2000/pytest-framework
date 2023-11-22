from lib.todo_list import TodoList
from lib.todo import Todo

def test_incomplete_list_returns_todos_list():
    todo_list = TodoList()
    todo1 = Todo("Walk dog")
    todo2 = Todo("Go swimming")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo2.mark_complete()
    assert todo1 in todo_list.incomplete()
    assert todo2 in todo_list.complete() 

def test_complete_list_returns_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Walk dog")
    todo2 = Todo("Go swimming")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo1.complete
    assert todo2.complete 

