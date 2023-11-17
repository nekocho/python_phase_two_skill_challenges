# Remove completed task Class Design Recipe


## 1. Describe the Problem

"As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list."

* Mark tasks in list as completed
* Remove completed tasks from list


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE
from lib.task_manager import *
import pytest
class TaskManager:
    # User-facing properties:
    #   Tasks: string

    def __init__(self):
        # Parameters:
        #   task: string
        #   task_list: list

        pass # No code here yet
    
    def complete_task(self, task):
        # Parameters:
        #     task_completed: a string representing the completed task
        # Returns: 
        #     A list of tasks with completed task omitted
        # Side-effects:
        #     Throws an exception if task is not in list
        pass #No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a completed task
Removes item from list
"""
task_manager = TaskManager()
task_manager.add_task("Walk the dog")
task_manager.add_task("Clean the house")
task_manager.complete_task("Walk the dog") 
task_manager.get_task_list() # "Task List: ['Clean the house']"

"""
Given two completed tasks
Removes all items from list
"""

task_manager = TaskManager()
task_manager.add_task("Walk the dog")
task_manager.add_task("Clean the house")
task_manager.complete_task("Walk the dog") 
task_manager.complete_task("Clean the house") 
task_manager.get_task_list() # "Task List: [None]"

"""
Given a completed task NOT in list
Throw an error
"""

task_manager = TaskManager()
task_manager.complete_task("Walk the dog") # => Raise error: "Item not in list!"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

