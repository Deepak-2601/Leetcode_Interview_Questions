def toGoatLatin(sentence):
        vowels = "aeiouAEIOU"
        words = sentence.split()
        result = []
        for i, word in enumerate(words, start=1):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += "a" * i
            result.append(goat_word)
        return " ".join(result)

 
sentence = "I speak Goat Latin"
print(toGoatLatin(sentence))