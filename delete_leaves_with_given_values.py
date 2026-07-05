class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root, target):
    if not root:
        return None
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if not root.left and not root.right and root.val == target:
        return None
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(2)

root = removeLeafNodes(root, 2)
print(root.val)
