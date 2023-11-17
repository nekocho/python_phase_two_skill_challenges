# Task Manager Class Design Recipe


## 1. Describe the Problem

"As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them."

* Start with an empty task manager
* Add items to the task manager
* View a list of added tasks


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskManager:
    # User-facing properties:
    #   Tasks: string

    def __init__(self):
        # Parameters:
        #   task: string
        #   task_list: list

        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def get_task_list(self):
        # Returns:
        #   A string of tasks added
        #   Optional: Create a formatted string
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
Adds task to list
Returns task from list in a formatted way
"""
task_manager = TaskManager()
task_manager.add_task("Walk the dog") # => ["Walk the dog"]

"""
Given another task
Adds task to list
Returns task from list in a formatted way
"""
task_manager = TaskManager()
task_manager.add_task("Walk the dog") 
task_manager.add_task("Clean the house") # => ["Walk the dog", "Clean the house"]


"""
Given no task
Returns None in task list
"""
task_manager = TaskManager()
task_manager.get_task_list() # "Task List:" None


"""
Given multiple tasks
Returns task list in a formatted way
"""
task_manager = TaskManager()
task_manager.add_task("Walk the dog") 
task_manager.add_task("Clean the house")
task_manager.get_task_list() # "Task List: ["Walk the dog", "Clean the house"]"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

