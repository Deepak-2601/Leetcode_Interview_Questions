def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1

nums = [1, 7, 3, 6, 5, 6]
result = pivot_index(nums)
print(f"The pivot index is: {result}") 