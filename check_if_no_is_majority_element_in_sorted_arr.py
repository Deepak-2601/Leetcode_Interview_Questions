def isMajorityElement(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count > len(nums) / 2

nums = [2,4,5,5,5,5,5,6,6]
target = 5
print(isMajorityElement(nums, target))