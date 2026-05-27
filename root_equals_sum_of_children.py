class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root):
    return root.val == root.left.val + root.right.val

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
print(checkTree(root))
