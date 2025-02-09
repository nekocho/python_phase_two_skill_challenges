class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = self.contents.split()
        # Kay's example
        self.read_so_far = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return self.title + ": " + self.contents

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return len(self.words) / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.


        # Kay's example:
        words_user_can_read = wpm * minutes
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = self.words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)




            # i = 0
            # text_chunk = []
            # while i < minutes:
            #     string = " ".join(self.words[i * wpm:(i + 1) * wpm])
            #     text_chunk.append(string)
            #     i += 1
                
            # return text_chunk
    
diary = DiaryEntry("test", "This is a longer diary entry")
diary.reading_chunk(2, 3)