def addBoldTag(s, words):
    n = len(s)
    bold = [False] * n
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                bold[i] = True
            start = s.find(word, start + 1)
    result = []
    i = 0
    while i < n:
        if bold[i]:
            result.append('<b>')
            while i < n and bold[i]:
                result.append(s[i])
                i += 1
            result.append('</b>')
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)

s = "abcxyz123"
words = ["abc", "123"]
result = addBoldTag(s, words)
print("Result with bold tags:", result)