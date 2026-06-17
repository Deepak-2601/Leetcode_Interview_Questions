class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sufficientSubset(root, limit):
    if not root:
        return None

    if not root.left and not root.right:
        return root if root.val >= limit else None

    root.left = sufficientSubset(root.left, limit - root.val)
    root.right = sufficientSubset(root.right, limit - root.val)

    return root if root.left or root.right else None


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(1)
root.right.left = TreeNode(17)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(3)
root.left.left.right = TreeNode(5)
limit = 22
result = sufficientSubset(root, limit)

from collections import deque

def printLevelOrder(root):
    if not root:
        return
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


printLevelOrder(result)