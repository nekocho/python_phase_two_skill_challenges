Grammar Check Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem


As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter 
Ends with a suitable sentence-ending punctuation mark.


2. Design the Function Signature

def check_gammar(text):
    Goes through a string to check if the first letter is capitalised and check if sentence ends with appropriate punctuation mark

Parameters:
    text - A string of text with or without capitalisation or punctuation

Returns:
    new text with correct capitalisation or punctuation


3. Create Examples as Tests

"""
Given a string of text
If string contains capitalised first letter and full stop at end of sentence
Returns string
"""

check_grammar("Hi my name is Fiona.") => "Hi my name is Fiona."

"""
Given a string of text without capitalisation
Returns string with capitalised first letter
"""

check_grammar("today's weather is sunny.") => "Today's weather is sunny."

"""
Given a string of text without capitalisation or punctuation at the end
Returns string with capitalised first letter and full stop
"""

check_grammar("today has been quite cold") => "Today has been quite cold.

"""
Given no string
Throws an error
"""
check_grammar("") => "No text provided!" 



4. Implement the Behaviour

check lib/grammar_check.py tests/test_grammar_check.py