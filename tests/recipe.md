
## Describe Problem

As a user
to help manage my time
I want to see estimate of reading time for a text, assuming that I can read 200 words a minute.

1 minute = 200 words read

300 is average word count per page

read_time function that takes string as argument. 
.split the text and record the len of it. Assign this value to word_count
Divide word_count by 200 and assign to reading_estimate
return the rounded figure of reading_estimate

call it 





## Design


def read_time(string):
    word_count = len(text.split()) 
    reading_estimate = word_count / 200            
    return round(reading_estimate)        

read_time(string) = "The quick brown fox jumps over the lazy dog"


# Test Examples
def test_read_time():
    test_text = "The quick brown fox jumps over the lazy dog"
    result = read_time(test_text)
    expected = round(len(test_text.splitt()) / 200 )
    assert result == expected

# Implement Behaviour




## ___________________________________________________________________________________


## Describe Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

capital letter at beginning
ends with . ? !

Boolean Output

Check that first char in text is capitalised AND last character in string == [".", "?", "!]
    return True
else
    return False




## Design

def check_grammar():
    list = [".", "?", "!"]
    if text[0].isupper() and text[-1] is in list
        return True
    else:
        return False


## Test Examples

def test_expected_output():
    result = check_grammar("hello world")
    assert result == False
 
    result = check_grammar("Hello world!")
    assert result == True

    result = check_grammar("Hello world")
    assert result == False

    result = check_grammar(hello world!")
    assert result == False





## Implement Behaviour




___________________________________________________________________________


###### Describe Problem


As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO


text = "#TODO: Shopping, Reading, Bath, Bed, Cook, Drive"

"#TODO" in text
return Boolean 
Return True






###### Design Function Square

def find_remind(text):
    if "#TODO" in text:
        return True
    else:
        return False
        


text = "#TODO: Shopping, Reading, Bath, Bed, Cook, Drive"
find_remind(text)




def find_remind(text)
    return "#TODO" in text

text = "#TODO: Shopping, Reading, Bath, Bed, Cook, Drive"
result = find_remind(text)
print(result)



###### Create Examples as Test

def test_find_remind_True():
    test_text = "#TODO: Shopping, Reading, Bath, Bed, Cook, Drive"
    result = find_remind(test_text)
    assert result == True

def test_find_remind_False():
    test_text = "#: Shopping, Reading, Bath, Bed, Cook, Drive"
    result = find_remind(test_text)
    assert result == False








###### Implement Behaviour 



____________________________________________________________________________________




###### Describe Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them




###### Design Function Square

initialise an empty list called #TODO
strings as entry to list. 



###### Create Examples as Test

   def_test_empty_list_returns_empty():
    todo_list = todo_list()
    result = todo_list()
    assert return "All tasks complete"


   def_test_list_of_one_returns_one():
    todo_list = todo_list()
    result = todo_list("Do shopping")
    assert return "Do shopping"


   def_test_list_of_three_returns_three():
    todo_list = todo_list()
    result = todo_list("Do Shopping, Read Book, Pick up Child")
    assert return "Do Shopping, Read Book, Pick up Child"



###### Implement Behaviour 


def todo_list(string):
    def __init__(self):
    self.tasks = []


    def add_task(self, task):
        self.tasks.append()











###### Describe Problem


As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

###### Design Function Square
###### Create Examples as Test
###### Implement Behaviour 