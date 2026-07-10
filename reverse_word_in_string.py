def reverseWords(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


s = "Hello World"
result = reverseWords(s)
print(result) 