def nextGreatestLetter(letters, target):
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]

l = ["c", "f", "j"]
t = "a"
print(nextGreatestLetter(l, t))