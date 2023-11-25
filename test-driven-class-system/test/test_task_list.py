from lib.task_list import TaskList

def test_task_list_incomplete_is_initially_empty():
    task_list = TaskList()
    assert task_list.all_complete() == []

def test_task_list_complete_is_initially_empty():
    task_list = TaskList()
    assert task_list.all_complete() == []