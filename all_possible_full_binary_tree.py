class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPossibleFBT(n):
    if n % 2 == 0:
        return []
    if n == 1:
        return [TreeNode(0)]
    result = []
    for left_nodes in range(1, n, 2):
        right_nodes = n - 1 - left_nodes
        for left_tree in allPossibleFBT(left_nodes):
            for right_tree in allPossibleFBT(right_nodes):
                root = TreeNode(0)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result

n = 7
result = allPossibleFBT(n)
print(f"Number of full binary trees with {n} nodes: {len(result)}")