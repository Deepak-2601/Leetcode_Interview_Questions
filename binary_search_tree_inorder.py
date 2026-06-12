class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root):
    if not root:
        return None
    stack = []
    current = root
    new_root = None
    prev = None
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if not new_root:
            new_root = TreeNode(current.val)
            prev = new_root
        else:
            prev.right = TreeNode(current.val)
            prev = prev.right
        current = current.right
    return new_root


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
root.left.left.left = TreeNode(1)
new_root = increasingBST(root)
current = new_root
while current:
    print(current.val)
    current = current.right
