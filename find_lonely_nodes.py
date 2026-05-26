class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLonelyNodes(root):
    lonely_nodes = []
    
    def dfs(node):
        if not node:
            return
        if node.left and not node.right:
            lonely_nodes.append(node.left.val)
        if node.right and not node.left:
            lonely_nodes.append(node.right.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return lonely_nodes

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(findLonelyNodes(root))