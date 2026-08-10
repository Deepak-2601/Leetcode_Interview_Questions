def countGoodStrings(words, chars):
    char_count = {}
    for c in chars:
        char_count[c] = char_count.get(c, 0) + 1
    total_length = 0
    for word in words:
        word_count = {}
        for c in word:
            word_count[c] = word_count.get(c, 0) + 1
        is_good = True
        for char, count in word_count.items():
            if char_count.get(char, 0) < count:
                is_good = False
                break
        if is_good:
            total_length += len(word)
    return total_length

words = ["cat", "bt", "hat", "tree"]
chars = "atach"
result = countGoodStrings(words, chars)
print(result)