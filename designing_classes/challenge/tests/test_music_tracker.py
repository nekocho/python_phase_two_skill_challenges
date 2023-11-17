from lib.music_tracker import *
import pytest

"""
Given a track
Add to music list
"""

def test_add_one_track_to_music_list():
    music_tracker = MusicTracker()
    actual = music_tracker.add_music("Toxic by Britney Spears")
    expected = ["Toxic by Britney Spears"]
    assert actual == expected

"""
Given a second track
Add to existing music list
"""
def test_add_two_tracks_to_music_list():
    music_tracker = MusicTracker()
    music_tracker.add_music("Toxic by Britney Spears")
    actual = music_tracker.add_music("I want it that way by The Backstreet Boys")
    expected = ["Toxic by Britney Spears", "I want it that way by The Backstreet Boys"]
    assert actual == expected

"""
When requesting music list
Return list in a formatted string
"""
def test_return_music_list_in_formatted_string():
    music_tracker = MusicTracker()
    music_tracker.add_music("Toxic by Britney Spears") 
    music_tracker.add_music("I want it that way by The Backstreet Boys")
    actual = music_tracker.format_list()
    expected = "Track list: ['Toxic by Britney Spears', 'I want it that way by The Backstreet Boys']"
    assert actual == expected


"""
When requesting music list but EMPTY
Throw an error
"""

def test_if_music_list_is_empty_throw_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.format_list() 
    error_message = str(e.value)
    assert error_message == "No tracks added"