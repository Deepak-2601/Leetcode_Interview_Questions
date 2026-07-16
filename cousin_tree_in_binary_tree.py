class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x, y):
    if not root:
        return False
    queue = [(root, None)]  
    while queue:
        level_size = len(queue)
        x_parent = y_parent = None
        for _ in range(level_size):
            node, parent = queue.pop(0)
            if node.val == x:
                x_parent = parent
            elif node.val == y:
                y_parent = parent
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        if x_parent and y_parent:
            return x_parent != y_parent 
        if x_parent or y_parent:
            return False 
    return False 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
print(isCousins(root, 4, 5)) 