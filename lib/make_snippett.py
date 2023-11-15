def make_snippet(string):
    words = string.split()
    if len(words) > 5:
        return " ".join(words[:5]) + "..."
    else:
        return " ".join(words)


string = "This string does have about six words"
snippet = make_snippet(string)
print(snippet)

     