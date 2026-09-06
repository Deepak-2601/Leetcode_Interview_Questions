def commonChars(words):
    if not words:
        return []
    char_count = [0] * 26
    for char in words[0]:
        char_count[ord(char) - ord('a')] += 1
    for word in words[1:]:
        current_count = [0] * 26
        for char in word:
            current_count[ord(char) - ord('a')] += 1
        for i in range(26):
            char_count[i] = min(char_count[i], current_count[i])
    result = []
    for i in range(26):
        result.extend([chr(i + ord('a'))] * char_count[i])    
    return result

words = ["bella", "label", "roller"]
result = commonChars(words)
print(result)
