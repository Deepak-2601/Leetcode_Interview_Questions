def repeatedSubstringPattern(s):
    if not s:
        return False
    doubled_s = (s + s)[1:-1]
    return s in doubled_s

s = "abab"
print(repeatedSubstringPattern(s))