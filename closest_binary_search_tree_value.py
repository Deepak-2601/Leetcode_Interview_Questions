class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root, target):
    closest = root.val
    while root:
        if (abs(root.val - target), root.val) < (abs(closest - target), closest):
            closest = root.val
        root = root.left if target < root.val else root.right
    return closest

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
t = 3.714286
print(closestValue(root, t))