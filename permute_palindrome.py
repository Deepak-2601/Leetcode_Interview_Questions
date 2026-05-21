def canPermutePalindrome(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1


s = "carrace"
print(canPermutePalindrome(s)) 