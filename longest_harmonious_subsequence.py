from collections import Counter
def findLHS(nums):
    freq = Counter(nums)
    longest = 0
    for num in freq:
        if num + 1 in freq:
            longest = max(longest, freq[num] + freq[num + 1])
    return longest

nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums)) 


