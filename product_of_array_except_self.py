def productExceptSelf(nums):
    length = len(nums)
    answer = [1] * length
    prefix_product = 1
    for i in range(length):
        answer[i] = prefix_product
        prefix_product *= nums[i]
    suffix_product = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]
    return answer

n = [1, 2, 3, 4]
result = productExceptSelf(n)
print("Product of array except self:", result)