def largeGroupPositions(s):
    result = []
    n = len(s)
    i = 0
    while i < n:
        start = i
        while i < n and s[i] == s[start]:
            i += 1
        end = i - 1
        if end - start + 1 >= 3:
            result.append([start, end])
    return result

s = "abbxxxxzzy"
large_groups = largeGroupPositions(s)
print(large_groups)
