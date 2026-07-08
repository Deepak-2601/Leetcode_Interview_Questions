class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    if not root:
        return []   
    result = []
    current_level = [root]
    left_to_right = True
    while current_level:
        level_values = []
        next_level = []
        for node in current_level:
            level_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not left_to_right:
            level_values.reverse()
        result.append(level_values)
        current_level = next_level
        left_to_right = not left_to_right
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(zigzagLevelOrder(root))