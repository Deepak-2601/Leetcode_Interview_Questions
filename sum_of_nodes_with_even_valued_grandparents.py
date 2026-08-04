class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root):
    def dfs(node, parent_val, grandparent_val):
        if not node:
            return 0
        total = 0
        if grandparent_val % 2 == 0:
            total += node.val
        total += dfs(node.left, node.val, parent_val)
        total += dfs(node.right, node.val, parent_val)
        return total

    return dfs(root, 1, 1)

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
result = sumEvenGrandparent(root)
print(result)