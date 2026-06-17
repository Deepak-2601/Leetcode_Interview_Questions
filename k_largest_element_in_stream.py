class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        self.nums = self.nums[:self.k]
        return self.nums[-1]
    
k = 3
nums = [4, 5, 8, 2]
kth_largest = KthLargest(k, nums)
print(kth_largest.add(3))  
print(kth_largest.add(5))   
print(kth_largest.add(10))  
print(kth_largest.add(9)) 
print(kth_largest.add(4))