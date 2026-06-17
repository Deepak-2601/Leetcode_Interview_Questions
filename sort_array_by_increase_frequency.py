def frequencySort(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    def sort_key(x):
        return (freq[x], -x)
    nums.sort(key=sort_key)
    return nums

nums = [2, 3, 1, 3, 2]
result = frequencySort(nums)
print(result)

