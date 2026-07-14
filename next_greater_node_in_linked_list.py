class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    answer = [0] * len(values)
    stack = []
    for i in range(len(values) - 1, -1, -1):
        while stack and stack[-1] <= values[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(values[i])
    return answer

head = ListNode(2, ListNode(1, ListNode(5)))
result = nextLargerNodes(head)
print(result)