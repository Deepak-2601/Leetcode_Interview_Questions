class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
    def inorderTraversal(root):
        if not root:
            return []
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    elements1 = inorderTraversal(root1)
    elements2 = inorderTraversal(root2)
    merged_elements = []
    i, j = 0, 0
    while i < len(elements1) and j < len(elements2):
        if elements1[i] < elements2[j]:
            merged_elements.append(elements1[i])
            i += 1
        else:
            merged_elements.append(elements2[j])
            j += 1
    while i < len(elements1):
        merged_elements.append(elements1[i])
        i += 1
    while j < len(elements2):
        merged_elements.append(elements2[j])
        j += 1
    return merged_elements

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

result = getAllElements(root1, root2)
print(result)