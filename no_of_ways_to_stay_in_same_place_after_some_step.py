def numWays(steps, arrLen):
    mod = 10**9 + 7
    max_pos = min(steps // 2 + 1, arrLen) 
    dp = [0] * max_pos
    dp[0] = 1  
    for _ in range(steps):
        new_dp = [0] * max_pos
        for pos in range(max_pos):
            new_dp[pos] = dp[pos] 
            if pos > 0:
                new_dp[pos] += dp[pos - 1]
            if pos < max_pos - 1:
                new_dp[pos] += dp[pos + 1]
            new_dp[pos] %= mod
        dp = new_dp
    return dp[0]

arrLen = 4
steps = 4
result = numWays(steps, arrLen)
print(f"Number of ways to stay at index 0 after {steps} steps in and array of length {arrLen}: {result}")
