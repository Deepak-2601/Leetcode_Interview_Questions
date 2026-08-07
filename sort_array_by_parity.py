def sortArrayByParity(nums):
    even_nums = []
    odd_nums = []
    
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    return even_nums + odd_nums

nums = [3, 1, 2, 4]
sorted_array = sortArrayByParity(nums)
print(sorted_array)