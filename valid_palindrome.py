def isPalindrome(s):
    filtered_chars = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_chars == filtered_chars[::-1]

s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)