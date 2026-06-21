def  reverseStr(s, k):
    res = list(s)
    for i in range(0, len(s), 2 * k):
        res[i:i + k] = reversed(res[i:i + k])
    return ''.join(res)

s = "abcdefg"
k = 2
print(reverseStr(s, k))