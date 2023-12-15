# DIARY Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

Nouns - Objects
Experience
Diary
Past Entry
Reading time
Reading speed
Tasks
Todo list
Contacts
Mobile numbers

Verbs - Methods
Record
Reflect
Read
Select
Keep track
Keep a list of tasks
See a list of numbers


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
    ┌──────────────────┐
    │DiaryEntry        │
    │- Entry           │
    │- Calculate total │
    │  words           │
    └────────┬─────────┘
             │
    ┌────────▼─────────┐        ┌────────────────┐
    │Diary             │        │ Contacts       │
    │- addEntry()      │        │ - Add contacts │
    │- view diary entry│◄───────┤                │
    │- view entry with │        └────────────────┘
    │reading time and  │        
    │reading speed     │
    │- view todolist   │
    │- view contacts   │
    └────────▲─────────┘
             │
             │
     ┌───────┴─────────┐
     │ ToDoList()      │
     │ - Add Task      │
     └─────────────────┘

```

_Also design the interface of each class in more detail._

```python
class Diary:
    def add_entry(self, entry):

    def view_diary(self):
    
    def read_diary_with_reading_time(self, wpm, minutes):
    
    def add_task(self, task):

    def todo_list(self):

    def add_contact(self, name, number):

    def contacts_list(self):




class DiaryEntry:
    # User-facing properties:
    #   entry: a string

    def __init__(self, entry):
        # Parameters:
        #   entry: a string
        # Side-effect:
        #   sets class property
        pass # No code here yet

    def count_words(self):
        # Returns:
        #   integer with number of words
        pass # No code here yet


class Task:
    # User-facing properties:
    #   task: a string

    def __init__(self, task):
        # Parameters:
        #   task: a string
        # Side-effect:
        #   sets class property
        pass # No code here yet


class Contacts:
    # User-facing properties:
    #   name: a string
    #   number: integer

    def __init__(self, name, number):
        # Parameters:
        #   name: a string
        #   number: integer
        # Side-effect:
        #   sets class property
        pass # No code here yet
    





```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

