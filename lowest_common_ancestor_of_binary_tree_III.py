class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(p, q):
    ancestors = set()
    while p:
        ancestors.add(p)
        p = p.parent
    while q:
        if q in ancestors:
            return q
        q = q.parent
    return None

root = Node(3)
root.left = Node(5)
root.left.parent = root
root.right = Node(1)
root.right.parent = root
root.left.left = Node(6)
root.left.left.parent = root.left
root.left.right = Node(2)
root.left.right.parent = root.left
root.left.right.left = Node(7)
root.left.right.left.parent = root.left.right
root.left.right.right = Node(4)
root.left.right.right.parent = root.left.right
root.right.left = Node(0)
root.right.left.parent = root.right
root.right.right = Node(8)
root.right.right.parent = root.right
p = root.left
q = root.right
lca = lowestCommonAncestor(p, q)
print("Lowest Common Ancestor:", lca.val)  # Output: 3