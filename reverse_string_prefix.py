def reverse_prefix(s, k):
    prefix = s[:k]
    suffix = s[k:]
    reversed_prefix = prefix[::-1]
    return reversed_prefix + suffix

s = "abcd"
k = 2
result = reverse_prefix(s, k)
print(result)