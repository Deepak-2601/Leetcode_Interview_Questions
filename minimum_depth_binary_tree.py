#  Minimum Depth of Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = minDepth(root)
print(result)