class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
    if not root:
        return 0
    if root.val < low:
        return rangeSumBST(root.right, low, high)
    elif root.val > high:
        return rangeSumBST(root.left, low, high)
    else:
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low = 7
high = 15
print(rangeSumBST(root, low, high))