class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self, head):
        self.head = head
    
    def getRandom(self):
        import random
        current = self.head
        result = current.val
        n = 1
        while current:
            if random.randint(0, n - 1) == 0:
                result = current.val
            current = current.next
            n += 1    
        return result
    
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
solution = Solution(node1)
print(solution.getRandom())