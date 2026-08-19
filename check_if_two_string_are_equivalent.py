def arrayStringsAreEqual(word1, word2):
    str1 = ''.join(word1)
    str2 = ''.join(word2)
    return str1 == str2

word1 = ["ab", "c"]
word2 = ["a", "bc"]
result = arrayStringsAreEqual(word1, word2)
print(result) 