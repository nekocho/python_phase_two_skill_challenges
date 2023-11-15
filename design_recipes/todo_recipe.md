Check TODO Function Design Recipe

1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

def check_todo(text)
    Check if body of text contains the string "#TODO"

Parameters:
    Text - Body of text that needs checking

Returns:
    Boolean if "#TODO" is present or not (True or False)


3. Create Examples as Tests

"""
Given a body of text
If no #TODO
returns False
"""

check_todo("I am not a to do list") => False

"""
Given a body of text
If contains #TODO
returns True
"""

check_todo("#TODO Groceries, Chores, Cleaning") => True

"""
Given no body of text
Throw an error
"""

check_todo("") => "No text found!"




4. Implement the Behaviour