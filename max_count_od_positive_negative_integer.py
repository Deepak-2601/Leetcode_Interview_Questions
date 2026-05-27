def maximumCount(nums):
    pos = 0
    neg = 0
    for num in nums:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    return max(pos, neg)

n = [-2, -1, -1, 1, 2, 3]
print(maximumCount(n))