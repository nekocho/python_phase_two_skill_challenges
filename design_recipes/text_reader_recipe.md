Text Reader Function Design Recipe

1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature

def text_reader(text):
    calculates length of time taken to read text

Parameters: 
    text: a string containing words (e.g. "I like to read")

Returns:
    Float that represents time taken to read text

Side effects:
    Interpolated string containing float that represents time taken to read text


3. Create Examples as Tests

"""
Given a body of text 200 words or over
It returns time taken to read the text
It prints time taken in a formatted string
"""
text_reader("_300 words in body of this text_") => "It would take you 1.5 minutes to read this text."

"""
Given a body of text with fewer than 200 words
It returns time taken to read the text
It prints string stating that it will take less than 1 minute to read
"""
text_reader("_150 words in body of this text_") => "It would take you 0.75 minutes to read this text."

"""
Given an empty string
Throws an error
It prints time taken in a formatted string
"""
text_reader("") => "No text entered"


4. Implement the Behaviour

Check lib/text_reader.py tests/test_text_reader.py
