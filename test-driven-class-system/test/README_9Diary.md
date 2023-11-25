### Describe Problem

As a user
To record my experiences
I want to keep a regular diary

To reflect on past experiences
I want to read past diary entries

So I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

So I can keep track of my tasks
I want to keep a todo list along with my diary

So I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

* Add todos, mark complete, list complete, incomplete 

### Design Class System


# Nouns
    Diary
    Diary Entries
    Experiences
    Time
    Reading Speed
    Todo List
    Tasks
    Phone numbers
    List of Phone numbers

# Verbs
    Record
    Keep
    Reflect
    Read
    Select
    Keep
    See a list
    Mark complete
    List complete
    List incomplete
    Add

class Diary():
    def add(self, diary_entry):
        # diary_entry: instance of DiaryEntry
        # returns nothing
        # side-effects: adds to list of diary entries
    
    def all(self):
        # returns a list of DiaryEntry instances

class DiaryEntry():
    # Public properties:
    #       title: a string representing an entry title
    #       contents: a string representing entry contents

    def __init__(self, title, contents):
    # title: a string representing an entry title
    # contents: a string representing entry contents 
    # side-effectsL sets the above properties

class TaskList():
    def add(self, task)
        # task: an instance of Task
        # returns nothing
        # side effect: adds to list of tasks

    def all_incomplete(self):
        # returns a list of instances of Task
        #   representing the incomplete tasks

    def all_complete(self):
        # returns a list of instances of task
        #   representing teh complete task

class Task():
    # public properties:
    # title: a string representing a job to do
    def __init__(self, title):
        # title: a string representing a job to do
        # side-effect: sets title property
        pass

    def mark_complete(self):
    # side-effect: marks teh task as complete
    # returns nothing


class PhoneNumberExtractor():
    def __init__(self, diary):
    # diary: an isntance of Diary
    # side-effect: set diary property

    def extract(self):
    # returns a list of strings representing
    #   a list of phone numbers


class ReadableEntryExtractor():
    def __init__(self, diary):
    # diary: an isntance of Diary
    # side-effect: set diary property

    def extract(self, wpm, minutes):
    # wpm: integer
    # returns longest diary entry that cna be read in 
    #   time given the wpm and minutes


## Create examples as Integration Tests

create examples of the classes being used together in different situations
and combinations that reflect the ways in which the system will be used. 

"""
When I add multiple diary entries
#all lists them out in the order they were added
"""

diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My Contents 1")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() # => [entry_1, entry_2, entry_3]

"""
When I add multiple tasks
and I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() # => [task_1, task_2, task_3]

"""
When I add multiple tasks
and I don't mark any complete
#all_incomplete lists only lists the incomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() # => [task_1, task_3]


"""
When I add multiple tasks
and I don't mark any complete
#all_complete only lists the iomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_complete() # => [task_2]


"""
When I add multiple tasks
and I call PhoneNumberExtractor #extract
i get a list of phone numbers from all diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 078000000 and 07800000001")
entry_2 = DiaryEntry("My Title 2", "My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My friend is 078000002")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["078000000", "07800000001", "078000002"]


"""
When I add multiple tasks
and I call PhoneNumberExtractor #extract
It ignores dublicate numbers 
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 078000000 and 078000000")
entry_2 = DiaryEntry("My Title 3", "My friend is 078000000")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["078000000"]





"""
When I add a diary entry
and I call PhoneNumberExtractor #extract
It ignores non-valid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 078000000 and 07800000001 and 07800, 13141")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []


"""
When I add no diary entries   
And i call PhoneNumberExtractor #extract
It returns empty list
"""

diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []



"""
When I add one diary entry that fits in the time
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It gets that diary entry
"""

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_1


"""
When I add one diary entry that does not fit in the time
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns None
"""

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => None




"""
When I add multiple diary entries, one readable 
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns the readable one
"""

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_2



"""
When I add multiple diary entries, multiple readable 
And i call ReadableEntryExtractor #extract
with a wpm of 2 and a minutes fo 2
It returns the longest readable one
"""

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
entry_3 = DiaryEntry("Title", "one two three")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_2




"""
When I add no diary entries   
And i call ReadableEntryExtractor #extract
It returns None
"""

diary = Diary()
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_2


# Create examples as Unit test
create examples of the behaviour of each relevant class at a more granualr level of detail

# Diary
    # initially diary has no entries
    diary = Diary()
    diary.all() # => []

# DiaryEntry
    # DiaryEntry is constructed with a title and contents
    entry = DiaryEntry("My Title", "My Contents")
    entry.title # => "My Title"
    entry.contents # => "My Contents

# TaskLis t
    # initially, TaskList has no incomplete tasks 
    task_list = TaskList()
    task_list.all_incomplete() # => []

    # initially, TaskList has no complete tasks 
    task_list = TaskList()
    task_list.all_complete() # => []

# Task
    # Task constructs with a title
    task = Task("Walk the dog")
    task.title # => "Walk the dog"





1 file per class 
4x classes

    Diary
    - Manage DiaryEntry objects
    - Add new entry
    - Retrieve past entries based on reading time/speed

    - List of DiaryEntry objects

    - add_entry(entry): adds new DiaryEntry to Diary
    - get_entry_by_reading_time(time, wpm)

    DiaryEntry
    - Contains individual diary entries
    - Include wpm / estimated read time for each entry?

    - instance of toDolist if integrating toDoList with each entry

    -  calc_reading_time(wpm)


    toDolist
    - List of toDo strings

    - add_task(task)
    - remove_task(task)
    - mark_complete(task)

    ContactList
    - Find all phone numbers and create contact list from that 
    - get_all_contacts(): returns all extracted contacts



### Create Examples as Integration Tests

Adding Entry and Retrieving by Reading Time:
- Create a Diary and add several DiaryEntry objects with varying lengths.
- Test retrieving entries that can be read in a given time at a certain reading speed.

Todo List Integration:
- Add a DiaryEntry with associated TodoList.
- Test adding tasks to the TodoList and retrieving them through the DiaryEntry.

Contact Extraction:

Create a DiaryEntry with text containing phone numbers.
Test extracting these numbers into a ContactList.




### Create Examples as Unit Tests

DiaryEntry:
Test creating entry and calculating its reading time.

TodoList:
Test adding, removing and marking tasks as complete.

ContactList:
Test extraction of numbers from a string or DiaryEntry.


### Implement the Behaviour 

