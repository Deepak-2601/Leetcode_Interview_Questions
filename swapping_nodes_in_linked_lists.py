class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    first = head
    second = head
    for _ in range(k - 1):
        first = first.next
    first_val = first.val
    temp = first
    while temp.next:
        temp = temp.next
        second = second.next
    first.val, second.val = second.val, first_val
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
head = swapNodes(head, k)
print("Swapped List:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
