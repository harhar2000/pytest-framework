from lib.task import Task


def test_task_constructs():
    task = Task("Walk the dog")
    assert task.title  == "Walk the dog"
"""
Newly constructed tasks are not complete
"""
def test_task_constructs_incomplete_tasks():
    task = Task("Walk the dog")
    assert not task.complete


"""
When I mark a task as complete
It is refelcted int eh complete property
"""
def test_marks_tasks_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.complete == True