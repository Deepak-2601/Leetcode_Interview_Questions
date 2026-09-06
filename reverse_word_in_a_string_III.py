def reverse_words(s):
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

s = "Hello World"
result = reverse_words(s)
print(result)