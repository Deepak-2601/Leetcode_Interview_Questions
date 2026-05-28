def smallest_index(s):
    n = len(s)
    for i in range(n):
        if s[i] == s[n - i - 1]:
            return i
    return -1

s = "abcacbd"
result = smallest_index(s)
print(result)