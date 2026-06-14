class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderSuccessor(root, p):
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
p = root.left
successor = inorderSuccessor(root, p)
if successor:
    print(successor.val)
