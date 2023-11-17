## Music Tracker Class Design Recipe


1. Describe the Problem

"As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them."

* Add a track listened to
* Show list of tracks
* Format the list


2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

``` python

class MusicTracker:
    def __init__(self):
        # Parameters:
        #     music list: list of tracks (unformatted)
        # Side-effects:
        #     music added from other function will be appended to music list
        pass
    
    def add_music(self, track):
        # Parameters:
        #     track: string of text with track name and artist
        # Side-effects:
        #     append track to music list
        pass
    
    def format_list(self):
        # Returns:
        #     music list in formatted way => "Track list: []"
        # Side-effects:
        #     Throws error if no track added
        pass


```
3. Create Examples as Tests

"""
Given a track
Add to music list
"""

music_tracker = MusicTracker()
music_tracker.add_music("Toxic by Britney Spears") => ["Toxic by Britney Spears"]

"""
Given a second track
Add to existing music list
"""
music_tracker = MusicTracker()
music_tracker.add_music("Toxic by Britney Spears") 
music_tracker.add_music("I want it that way by The Backstreet Boys") => ["Toxic by Britney Spears", "I want it that way by The Backstreet Boys"]

"""
When requesting music list
Return list in a formatted string
"""

music_tracker = MusicTracker()
music_tracker.add_music("Toxic by Britney Spears") 
music_tracker.add_music("I want it that way by The Backstreet Boys")
music_tracker.format_list() => "Track list: ['Toxic by Britney Spears', 'I want it that way by The Backstreet Boys']"

"""
When requesting music list but EMPTY
Throw an error
"""

music_tracker = MusicTracker()
music_tracker.format_list() => "No tracks added"



4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

