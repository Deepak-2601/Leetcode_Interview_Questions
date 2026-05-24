def mergeAlternately(word1, word2):
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    merged.append(word1[i:])
    merged.append(word2[j:])
    return ''.join(merged)


w1 = "abc"
w2 = "pqr"
result = mergeAlternately(w1, w2)
print(result) 
