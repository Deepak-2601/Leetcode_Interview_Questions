class NumArray(object):
    def __init__(self, nums):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
    

nums = [1, 2, 3, 4, 5]
num_array = NumArray(nums)
print(num_array.sumRange(1, 3))