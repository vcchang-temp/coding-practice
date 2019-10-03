# Reverse a singly linked list

# Input: Node head (could be null or of any length)

# Iterative approach
# Time: O(n)    -> traverse list with n nodes once
# Space: O(1)   -> in-place reversal

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head: ListNode):
    if head is None or head.next is None:
        return head
    
    back = head
    front = head.next
    ahead = head.next.next
    
    while ahead is not None:
        front.next = back
        back.next = None
        back = front
        front = ahead
        ahead = ahead.next

    if ahead is None:
        front.next = back
        if back.next is not None:
            back.next = None
        return front

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = node1
    actual = reverse(head)

    node1Rev = ListNode(1)
    node2Rev = ListNode(2)
    node3Rev = ListNode(3)
    node4Rev = ListNode(4)
    node4Rev.next = node3Rev
    node3Rev.next = node2Rev
    node2Rev.next = node1Rev
    expected = node4Rev

    testActual = actual
    testExpected = expected
    while testActual is not None:
        assert testActual.val == testExpected.val
        testActual = testActual.next
        testExpected = testExpected.next
    
    print("Yayy, reversed a linked list!")