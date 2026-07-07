def maximumProduct(nums):
    nums.sort()
    a = nums[0] * nums[1] * nums[-1]
    b = nums[-1] * nums[-2] * nums[-3]
    return max(a, b)


nums = [1, 2, 3, 4]
result = maximumProduct(nums)
print(result)