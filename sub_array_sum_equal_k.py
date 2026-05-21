def subarraySum(nums, k):
    count = 0
    sum_so_far = 0
    sum_counts = {0: 1}  
    for num in nums:
        sum_so_far += num
        if (sum_so_far - k) in sum_counts:
            count += sum_counts[sum_so_far - k]
        if sum_so_far in sum_counts:
            sum_counts[sum_so_far] += 1
        else:
            sum_counts[sum_so_far] = 1
    return count

nums = [1, 1, 1]
k = 2
result = subarraySum(nums, k)
print(result) 