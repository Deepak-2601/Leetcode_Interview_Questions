class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.left.right
lca = lowestCommonAncestor(root, p, q)
print("Lowest Common Ancestor of nodes {} and {} is: {}".format(p.val, q.val, lca.val))
