def minSubsequence(source, target):
    source_set = set(source)
    for char in target:
        if char not in source_set:
            return -1
    count = 0
    i = 0
    while i < len(target):
        j = 0
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
        count += 1
    return count


source = "abc"
target = "abcbc"
print(minSubsequence(source, target))