from random import choices
class Solution(object):
    def __init__(self, nums):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] not in self.dict:
                self.dict[nums[i]] = []
            self.dict[nums[i]].append(i)

    def pick(self, target):
        return choices(self.dict[target])
    
ans = Solution([1, 2, 3, 3, 3])
print(ans.pick(3))

