
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