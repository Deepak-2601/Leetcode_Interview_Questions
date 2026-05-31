def shortestDistance(wordsDict, word1, word2):
    min_distance = float('inf')
    index1, index2 = -1, -1

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            index1 = i
        elif wordsDict[i] == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            min_distance = min(min_distance, abs(index1 - index2))

    return min_distance

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(shortestDistance(wordsDict, word1, word2))