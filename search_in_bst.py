class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
    

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(searchBST(root, 2).val)