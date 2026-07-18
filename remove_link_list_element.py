class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

node7 = ListNode(6)
node6 = ListNode(5, node7)
node5 = ListNode(4, node6)
node4 = ListNode(3, node5)
node3 = ListNode(6, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

val = 6
new_head = removeElements(head, val)
print_linked_list(new_head)
