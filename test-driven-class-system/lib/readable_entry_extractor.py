class ReadableEntryExtractor():
    def __init__(self, diary):
        self._diary = diary
     
    def extract(self, wpm, minutes):
        longest_readable = None
        longest_readable_length = 0
        for entry in self._diary.all():
            if self._word_count(entry.contents) > longest_readable_length:
                if self._entry_readable_in_time(wpm, minutes, entry):
                    longest_readable = entry
                    longest_readable_length = self._word_count(entry.contents)
        return longest_readable

    
        
    def _entry_readable_in_time(self, wpm, minutes, entry):
        length_readable = wpm * minutes
        return self._word_count(entry.contents) <= length_readable
            

    def _word_count(self, string):
        return len(string.split(" "))