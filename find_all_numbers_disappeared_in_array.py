def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    return [i + 1 for i in range(n) if nums[i] > 0]

n = [4,3,2,7,8,2,3,1]
result = findDisappearedNumbers(n)
print(f"The disappeared numbers in the array are: {result}.")