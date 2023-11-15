def count_words(string):
    words = string.split()
    return len(words)

string = "How many words are in this string"
value = count_words(string)
print(value)