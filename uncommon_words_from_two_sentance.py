def  uncommonFromSentences(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    
    word_count = {}
    
    for word in words1:
        word_count[word] = word_count.get(word, 0) + 1
    
    for word in words2:
        word_count[word] = word_count.get(word, 0) + 1
    
    uncommon_words = []
    for word, count in word_count.items():
        if count == 1:
            uncommon_words.append(word)
    
    return uncommon_words

s1 = "this apple is sweet"
s2 = "this apple is sour"
result = uncommonFromSentences(s1, s2)
print(result)