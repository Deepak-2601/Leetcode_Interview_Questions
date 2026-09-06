# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    current = head
    while current and current.next:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair
        if prev:
            prev.next = second
        prev = current
        current = next_pair
    return new_head

MyLinkedList = ListNode(1)
MyLinkedList.next = ListNode(2)
MyLinkedList.next.next = ListNode(3)
MyLinkedList.next.next.next = ListNode(4)
result = swapPairs(MyLinkedList)
print(result.val)