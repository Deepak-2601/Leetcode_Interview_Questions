class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]
    paths = []
    for path in binaryTreePaths(root.left):
        paths.append(str(root.val) + "->" + path)
    for path in binaryTreePaths(root.right):
        paths.append(str(root.val) + "->" + path)
    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
result = binaryTreePaths(root)
print(result)