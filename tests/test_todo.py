from lib.todo import Todo 

def test_todo_initialisation():
    todo = Todo("Walk dog")
    assert todo.task == "Walk dog"
    assert not todo.complete
    
def test_mark_todo_complete():
    todo = Todo("Go shopping")
    todo.mark_complete()
    assert todo.complete