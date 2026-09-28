def minSteps(s,t):
    freq_s = {}
    for char in s:
        if char in freq_s:
            freq_s[char] += 1
        else:
            freq_s[char] = 1
    freq_t = {}
    for char in t:
        if char in freq_t:
            freq_t[char] += 1
        else:
            freq_t[char] = 1
    steps = 0
    for char in freq_s:
        if char in freq_t:
            steps += max(0, freq_s[char] - freq_t[char])
        else:
            steps += freq_s[char]
    return steps

s = "bab"
t = "aba"
result = minSteps(s,t)
print(result)