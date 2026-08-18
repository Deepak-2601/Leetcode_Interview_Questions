def find_missing_ranges(nums, lower, upper):
    missing_ranges = []
    prev = lower - 1 
    for num in nums:
        if num > prev + 1:  
            missing_ranges.append((prev + 1, num - 1))
        prev = num 
    if prev < upper:  
        missing_ranges.append((prev + 1, upper))
    return missing_ranges

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
missing_ranges = find_missing_ranges(nums, lower, upper)
print("Missing ranges:", missing_ranges)
