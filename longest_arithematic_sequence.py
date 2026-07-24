def longestArithSeqLength(nums):
    n = len(nums)
    if n <= 2:
        return n
    dp = [dict() for _ in range(n)]
    ans = 2
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            ans = max(ans, dp[i][diff])
    return ans


nums = [3,6,9,12]
print(longestArithSeqLength(nums))
