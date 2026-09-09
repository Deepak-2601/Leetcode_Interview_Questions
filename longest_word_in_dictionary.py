def longestWord(words):
    word_set = set(words)
    longest = ""
    for word in words:
        if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
            if all(word[:i] in word_set for i in range(1, len(word))):
                longest = word    
    return longest

w = ["w","wo","wor","worl","world"]
print(longestWord(w))