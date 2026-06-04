class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    elif not root1:
        return root2
    elif not root2:
        return root1
    else:
        merged = TreeNode(root1.val + root2.val)
        merged.left = mergeTrees(root1.left, root2.left)
        merged.right = mergeTrees(root1.right, root2.right)
        return merged
    

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
merged_tree = mergeTrees(root1, root2)
from collections import deque

merged_tree = mergeTrees(root1, root2)

result = []
queue = deque([merged_tree])

while queue:
    node = queue.popleft()

    if node:
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    else:
        result.append(None)

while result and result[-1] is None:
    result.pop()

print(result)