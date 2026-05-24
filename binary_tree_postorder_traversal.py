class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if root is None:
        return []
    result = []
    result.extend(postorderTraversal(root.left))
    result.extend(postorderTraversal(root.right))
    result.append(root.val)
    return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
result = postorderTraversal(root)
print(result)