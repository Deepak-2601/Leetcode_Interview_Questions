def maxSubArrayLen(nums, k):
    sum_map = {0: -1}  
    current_sum = 0
    max_length = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - k in sum_map:
            max_length = max(max_length, i - sum_map[current_sum - k])
        if current_sum not in sum_map:
            sum_map[current_sum] = i
    return max_length

nums = [1, -1, 5, -2, 3]
k = 3
result = maxSubArrayLen(nums, k)
print("Maximum length of subarray with sum k:", result)