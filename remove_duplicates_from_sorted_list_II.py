class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return None
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    while current:
        while current.next and current.val == current.next.val:
            current = current.next
        if prev.next == current:
            prev = prev.next
        else:
            prev.next = current.next
        current = current.next
    return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

result = deleteDuplicates(head)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")