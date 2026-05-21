def judgePoint24(cards):
    from itertools import permutations
    from operator import add, sub, mul, truediv

    def helper(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    for op in (add, sub, mul, truediv):
                        if op == truediv and nums[j] == 0:
                            continue
                        new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        new_nums.append(op(nums[i], nums[j]))
                        if helper(new_nums):
                            return True
        return False

    for perm in permutations(cards):
        if helper(list(perm)):
            return True
    return False


cards = [4, 1, 8, 7]
print(judgePoint24(cards))