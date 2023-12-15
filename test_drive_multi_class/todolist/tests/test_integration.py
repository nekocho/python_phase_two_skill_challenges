from lib.todo import *
from lib.todo_list import *

'''
When given a task to do
Add to todo list
Returns list of incomplete tasks
'''

def test_adding_task_to_todo_list():
    todolist = TodoList()
    task1 = Todo("Hoover")
    todolist.add(task1)
    actual = todolist.incomplete()
    expected = [task1]
    assert actual == expected

'''
When given multiple tasks to do
Add to todo list
Returns list of incomplete tasks
'''

def test_adding_multiple_task_to_todo_list():
    todolist = TodoList()
    task1 = Todo("Hoover")
    task2 = Todo("Clean Bedroom")
    todolist.add(task1)
    todolist.add(task2)
    actual = todolist.incomplete()
    expected = [task1, task2]
    assert actual == expected

'''
If a task is completed
Return separate list of completed task
'''

def test_list_completed_task():
    todolist = TodoList()
    task1 = Todo("Hoover")
    task2 = Todo("Clean Bedroom")
    task3 = Todo("Walk dog")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    task2.mark_complete()
    actual = todolist.complete()
    expected = [task2]
    assert actual == expected

'''
If multiple task is completed
Return separate list of completed task
'''

def test_list_completed_multiple_task():
    todolist = TodoList()
    task1 = Todo("Hoover")
    task2 = Todo("Clean Bedroom")
    task3 = Todo("Walk dog")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    task1.mark_complete()
    task3.mark_complete()
    actual = todolist.complete()
    expected = [task1, task3]
    assert actual == expected


'''
If multiple task given
When mark give up
mark all completed
'''

def test_list_giveup_multiple_task():
    todolist = TodoList()
    task1 = Todo("Hoover")
    task2 = Todo("Clean Bedroom")
    task3 = Todo("Walk dog")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    todolist.give_up()
    actual = todolist.complete()
    expected = [task1, task2, task3]
    assert actual == expected

