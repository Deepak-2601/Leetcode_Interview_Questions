def intersect(nums1, nums2):
    count_dict = {}
    for num in nums1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    intersection = []
    for num in nums2:
        if num in count_dict and count_dict[num] > 0:
            intersection.append(num)
            count_dict[num] -= 1
    return intersection

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))