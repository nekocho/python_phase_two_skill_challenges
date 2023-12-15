from lib.todo import *

'''
When given a task 
If completed, mark as True
'''

def test_task_complete():
    todo = Todo("Hoover")
    actual = todo.mark_complete()
    expected = True
    assert actual == expected

