def is_monotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False
    return increasing or decreasing

n = [1, 2, 2, 3]
result = is_monotonic(n)
print(f"The array is monotonic: {result}")