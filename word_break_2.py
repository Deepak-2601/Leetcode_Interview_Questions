def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [[] for _ in range(len(s) + 1)]
    dp[0] = [""]
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                for sentence in dp[j]:
                    dp[i].append((sentence + " " + s[j:i]).strip())
    return dp[len(s)]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))

