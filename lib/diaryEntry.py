class DiaryEntry:
    def __init__ (self, title, contents):
        self.title = title
        self.contents = contents
        

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return len(self.contents.split())
    

    def reading_time(self, wpm):
       total_words = self.count_words()
       time_in_mins = total_words / wpm
       rounded_time = round(time_in_mins)
       if rounded_time < 1:
        rounded_time = 1
       return rounded_time 

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        start = self.read_pointer
        end = min(self.read_pointer + words_to_read, len(self.words))
        self.read_pointer = end
        if self.read_pointer == len(self.words):
           self.read_pointer = 0
        return ' '.join(self.words[start:end])
    

class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0
  
    def check(self, text):
        list = [".", "?", "!"]
        self.total_texts += 1
        if text[0].isupper() and text[-1] in list:
            self.passed_texts += 1
            return True
        else:
            return False

    
    def percentage_good(self):
        # Check if no texts have been processed
        if self.total_texts == 0:
            return 0
        ratio = self.passed_texts / self.total_texts
        percentage = ratio * 100
   
        return percentage
