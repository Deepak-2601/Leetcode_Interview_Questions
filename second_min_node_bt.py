class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSecondMinimumValue(root):

    unique_values = set()
    def dfs(node):
        if node:
            unique_values.add(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    if len(unique_values) < 2:
        return -1
    min_value = min(unique_values)
    second_min = float('inf')
    for value in unique_values:
        if min_value < value < second_min:
            second_min = value
    return second_min if second_min != float('inf') else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(findSecondMinimumValue(root))


