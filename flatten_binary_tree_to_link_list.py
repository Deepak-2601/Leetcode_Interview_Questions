class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    current = root
    while current:
        if current.left:
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right
            
            rightmost.right = current.right
            current.right = current.left
            current.left = None
        current = current.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)

current = root
result = []
while current:
    result.extend([current.val, None])
    current = current.right
if result:
        result.pop()
print(result)