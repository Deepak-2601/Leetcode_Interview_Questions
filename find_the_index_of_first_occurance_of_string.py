def strStr(haystack, needle):
    if needle == "":
        return 0
    if haystack == "":
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))