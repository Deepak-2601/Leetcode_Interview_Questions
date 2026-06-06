class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root):
    values = []
    def in_order_traversal(node, values):
        if node:
            in_order_traversal(node.left, values)
            values.append(node.val)
            in_order_traversal(node.right, values)
    in_order_traversal(root, values)
    min_diff = float('inf')
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i - 1])
    return min_diff

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(minDiffInBST(root))