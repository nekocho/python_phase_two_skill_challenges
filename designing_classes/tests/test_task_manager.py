from lib.task_manager import *
import pytest


# Given a task
# Adds task to string
# Returns task list in a formatted string

def test_when_task_is_added():
    task_manager = TaskManager()
    actual = task_manager.add_task("Walk the dog")
    expected = ['Walk the dog']
    assert actual == expected

# Given another task
# Adds task to list
# Returns task from list with multiple items

def test_when_two_task_is_added():
    task_manager = TaskManager()
    assert task_manager.add_task("Walk the dog") == ['Walk the dog']
    assert task_manager.add_task("Clean the house") == ['Walk the dog', 'Clean the house']

# Given no task
# Returns None in task list

def test_when_no_task_list_is_None():
    task_manager = TaskManager()
    assert task_manager.get_task_list() == "Task List: [None]"

# Given multiple tasks
# Returns task list in a formatted way

def test_when_multiple_task_list_is_formatted():
    task_manager = TaskManager()
    task_manager.add_task("Walk the dog") 
    task_manager.add_task("Clean the house")
    assert task_manager.get_task_list() == "Task List: ['Walk the dog', 'Clean the house']"
