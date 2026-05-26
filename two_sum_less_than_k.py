def twoSumLessThanK(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_sum = -1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            max_sum = max(max_sum, current_sum)
            left += 1
        else:
            right -= 1
    return max_sum

nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(twoSumLessThanK(nums, k))