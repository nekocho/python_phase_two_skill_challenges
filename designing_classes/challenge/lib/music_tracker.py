class MusicTracker:
    def __init__(self):
        self.music_list = []
    
    def add_music(self, track):
        self.music_list.append(track)
        return self.music_list
    
    def format_list(self):
        if self.music_list == []:
            raise Exception("No tracks added")
        else:
            return f"Track list: {self.music_list}"
