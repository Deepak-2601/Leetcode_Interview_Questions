class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0
    sum = 0
    if root.left and not root.left.left and not root.left.right:
        sum += root.left.val
    sum += sumOfLeftLeaves(root.left)
    sum += sumOfLeftLeaves(root.right)
    return sum


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sumOfLeftLeaves(root))


