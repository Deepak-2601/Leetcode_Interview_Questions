def lengthOfLongestSubstringKDistinct(s,k):
    if k == 0:
        return 0
    left = 0
    right = 0
    char_count = {}
    max_length = 0
    while right < len(s):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length

s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))