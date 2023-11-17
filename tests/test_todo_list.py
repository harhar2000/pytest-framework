from lib.todo_list import ToDoList

def test_empty_list_returns_empty():
    todolist = ToDoList()
    result = todolist.show_tasks()
    assert result == "All tasks complete"


def test_list_of_one_returns_one():
    todolist = ToDoList()
    todolist.add_task("Do shopping")
    result = todolist.show_tasks()
    assert result == "Do shopping"


def test_list_of_three_returns_three():
    todolist = ToDoList()
    todolist.add_task("Do Shopping")
    todolist.add_task("Read Book")
    todolist.add_task("Pick up Child")
    result = todolist.show_tasks()
    assert result == "Do Shopping\nRead Book\nPick up Child"
