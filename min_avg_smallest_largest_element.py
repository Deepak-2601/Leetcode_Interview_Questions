def minimumAverage(nums):
    nums.sort()
    averages = []
    left = 0
    right = len(nums) - 1
    while left < right:
        current_average = (nums[left] + nums[right]) / 2.0
        averages.append(current_average)
        left += 1
        right -= 1
    return min(averages)

n = [7,8,3,4,15,13,4,1]
print(minimumAverage(n))