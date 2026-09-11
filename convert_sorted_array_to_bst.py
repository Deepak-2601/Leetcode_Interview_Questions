class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root

nums = [-10, -3, 0, 5, 9]
bst_root = sortedArrayToBST(nums)
print("root:", bst_root.val if bst_root else None)
print("left:", bst_root.left.val if bst_root and bst_root.left else None)
print("right:", bst_root.right.val if bst_root and bst_root.right else None)
print("left.left:", bst_root.left.left.val if bst_root and bst_root.left and bst_root.left.left else None)
print("left.right:", bst_root.left.right.val if bst_root and bst_root.left and bst_root.left.right else None)
print("right.left:", bst_root.right.left.val if bst_root and bst_root.right and bst_root.right.left else None)
print("right.right:", bst_root.right.right.val if bst_root and bst_root.right and bst_root.right.right else None)