class Diary: 
    def __init__(self):
       self.entries = []

    def add(self, entry):
       self.entries.append(entry)

    def count_words(self):
        return sum([entry.count_words() for entry in self.entries])