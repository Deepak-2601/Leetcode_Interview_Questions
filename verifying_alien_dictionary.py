def isAlienSorted(words, order):
    order_index = {char: index for index, char in enumerate(order)}
    
    def compare(word1, word2):
        for c1, c2 in zip(word1, word2):
            if order_index[c1] < order_index[c2]:
                return True
            elif order_index[c1] > order_index[c2]:
                return False
        return len(word1) <= len(word2)
    
    for i in range(len(words) - 1):
        if not compare(words[i], words[i + 1]):
            return False
    return True

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(words, order))