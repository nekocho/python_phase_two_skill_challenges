from lib.remove_completed_tasks import *
import pytest

# Given a completed task
# Removes item from list

def test_when_task_completed_omits_task():
    remove_completed = RemoveCompleted()
    remove_completed.add_task("Walk the dog")
    remove_completed.add_task("Clean the house")
    remove_completed.complete_task("Walk the dog") 
    assert remove_completed.get_task_list() == "Task List: ['Clean the house']"

# Given two completed tasks
# Removes all items from list

def test_when_task_completed_omits_task():
    remove_completed = RemoveCompleted()
    remove_completed.add_task("Walk the dog")
    remove_completed.add_task("Clean the house")
    remove_completed.complete_task("Walk the dog") 
    remove_completed.complete_task("Clean the house") 
    assert remove_completed.get_task_list() == "Task List: [None]"


# Given a completed task NOT in list
# Throw an error

def test_if_task_completed_is_not_in_list_throw_error():
    remove_completed = RemoveCompleted()
    with pytest.raises(Exception) as e:
        remove_completed.complete_task("Walk the dog")
    error_message = str(e.value)
    assert error_message == "Item not in List!"