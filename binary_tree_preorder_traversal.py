class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root is None:
        return []
    result = [root.val]
    result.extend(preorderTraversal(root.left))
    result.extend(preorderTraversal(root.right))
    return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
result = preorderTraversal(root)
print(result)